#!/usr/bin/python
# coding=UTF8
import tkinter
from tkinter import messagebox
import SvnUtils
import XMLParse
import ServerBoost
import SystemUtils


class SvnTool(object):
    def __init__(self):
        self.root = tkinter.Tk()  # 定义主窗口
        self.root.title("SvnTool")  # 主窗口标题
        self.root.geometry('380x180')  # 主窗口尺寸
        self.version = tkinter.IntVar()  # 分支值
        self.hide = tkinter.IntVar()  # 分支值
        self.stampStr = tkinter.StringVar()  # 时间戳
        self.configs = {}  # 路径配置
        self.serverPaths = []  # 服务器路径
        self.assetPath = ''  # 客户端路径
        self.excelPath = ''  # Excel 路径
        self.currentBranch = 0  # 已操作的分支
        self.nextBranch = 0  # 待操作的分支
        self.serverProcList = []  # 服务器进程列表
        self.dbProcList = []  # Redis 进程列表

        # 处理关闭窗口事件
        self.root.protocol('WM_DELETE_WINDOW', self.closeWindow)

        # 选择分支的三个选项
        self.choice1 = tkinter.Radiobutton(self.root, text="主干", variable=self.version, value=1)
        self.choice2 = tkinter.Radiobutton(self.root, text="线上分支", variable=self.version, value=2)
        self.choice3 = tkinter.Radiobutton(self.root, text="提审分支", variable=self.version, value=3)
        self.choice4 = tkinter.Checkbutton(self.root, text="仅显示func", variable=self.hide, onvalue=2, offvalue=0)

        # 更新按钮
        self.updateButton = tkinter.Button(self.root, text="拉取更新", command=self.updateCall)
        # 回退按钮
        self.revertButton = tkinter.Button(self.root, text="本地回退", command=self.revertCall)
        # 启动按钮
        self.boostButton = tkinter.Button(self.root, text="一键启服", command=self.boostCall)
        # 清档按钮
        self.flushButton = tkinter.Button(self.root, text="本地清档", command=self.flushCall)
        # 关服按钮
        self.shutButton = tkinter.Button(self.root, text="一键关闭", command=self.shutCall)
        # DB按钮
        self.redisButton = tkinter.Button(self.root, text="启动DB", command=self.redisCall)
        # DB按钮
        self.redisButton = tkinter.Button(self.root, text="启动DB", command=self.redisCall)
        # 时间戳按钮
        self.stampButton = tkinter.Button(self.root, text="时间戳转换", command=self.stampCall)

        # 时间戳文本框
        self.stampText = tkinter.Entry(self.root, width=15, textvariable=self.stampStr)
        pass

    def elementArrange(self):
        self.choice1.grid(row=1, column=0, sticky=tkinter.W, padx=40, ipady=8)
        self.choice2.grid(row=2, column=0, sticky=tkinter.W, padx=40, ipady=8)
        self.choice3.grid(row=3, column=0, sticky=tkinter.W, padx=40, ipady=8)
        self.updateButton.grid(row=1, column=2, padx=10)
        self.revertButton.grid(row=1, column=3, padx=10)
        self.boostButton.grid(row=2, column=2, padx=20)
        self.shutButton.grid(row=2, column=3, padx=20)
        self.flushButton.grid(row=3, column=3, padx=20)
        self.redisButton.grid(row=3, column=2, padx=20)
        self.stampText.grid(row=4, column=0, sticky=tkinter.E, ipadx=20)
        self.stampButton.grid(row=4, column=2, padx=20, pady=10)
        self.choice4.grid(row=4, column=3)

    def stampCall(self):
        try:
            stamp = self.stampStr.get()
            if stamp is None or stamp == '':
                messagebox.showinfo("Error", '请输入正确的时间戳')
            elif stamp.find('-') >= 0:
                time = SystemUtils.getStampFromDate(stamp)
                self.stampText.delete(0, 'end')
                self.stampText.insert(0, time)
            else:
                time = SystemUtils.getDateFromStamp(stamp)
                self.stampText.delete(0, 'end')
                self.stampText.insert(0, time)
        except Exception as e:
            self.stampText.delete(0, 'end')
            messagebox.showerror("Error", str(e))
        pass

    def updateCall(self):
        try:
            branch = self.version.get()
            if branch in (1, 2, 3):
                self.getPathFromXML(branch)
                SvnUtils.update(self.assetPath, self.excelPath, self.serverPaths, True)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def revertCall(self):
        try:
            messagebox.showwarning("Warning", "请手动回退")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def boostCall(self):
        try:
            branch = self.version.get()
            if self.hide.get() == 2:
                isHide = True
            else:
                isHide = False
            if branch in (1, 2, 3):
                self.getPathFromXML(branch)
                ports = ServerBoost.getPortsFromPaths(self.serverPaths)
                if not SystemUtils.isDBOpen(ports):
                    messagebox.showwarning("Warning", "请先启动DB！")
                else:
                    SystemUtils.killProcess(self.serverProcList)
                    SystemUtils.killServerProcess()
                    self.serverProcList = ServerBoost.serverBoost(self.serverPaths, isHide)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def flushCall(self):
        try:
            branch = self.version.get()
            self.nextBranch = branch
            if self.currentBranch != 0 and self.currentBranch != self.nextBranch:
                messagebox.showwarning("Warning", "请确保Branch相同")
            else:
                self.currentBranch = self.nextBranch
                if branch in (1, 2, 3):
                    flag = messagebox.askyesno("Warning", "确定清档吗？")
                    if flag:
                        self.getPathFromXML(branch)
                        ports = ServerBoost.getPortsFromPaths(self.serverPaths)
                        if not SystemUtils.isDBOpen(ports):
                            messagebox.showwarning("Warning", "请先启动DB！")
                        else:
                            ServerBoost.localFlush(self.serverPaths)
                            messagebox.showinfo("Done", "清档成功")
                else:
                    messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def shutCall(self):
        try:
            self.currentBranch = 0
            branch = self.version.get()
            if branch in (1, 2, 3):
                SystemUtils.killProcess(self.serverProcList + self.dbProcList)
                SystemUtils.killAllProcess()
                self.serverProcList = []
                self.dbProcList = []
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def redisCall(self):
        try:
            branch = self.version.get()
            self.currentBranch = branch
            if branch in (1, 2, 3):
                self.getPathFromXML(branch)
                SystemUtils.killProcess(self.dbProcList)
                self.dbProcList = ServerBoost.redisBoost(self.serverPaths)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def getPathFromXML(self, version):
        self.configs = XMLParse.getDictFromXML()

        if version == 1:
            if 'trunkAsset' in self.configs.keys():
                self.assetPath = self.configs['trunkAsset']
            if 'trunkServer' in self.configs.keys():
                self.serverPaths = self.configs['trunkServer']
            if 'trunkExcel' in self.configs.keys():
                self.excelPath = self.configs['trunkExcel']
        elif version == 2:
            if 'currentAsset' in self.configs.keys():
                self.assetPath = self.configs['currentAsset']
            if 'currentServer' in self.configs.keys():
                self.serverPaths = self.configs['currentServer']
            if 'currentExcel' in self.configs.keys():
                self.excelPath = self.configs['currentExcel']
        elif version == 3:
            if 'nextAsset' in self.configs.keys():
                self.assetPath = self.configs['nextAsset']
            if 'nextServer' in self.configs.keys():
                self.serverPaths = self.configs['nextServer']
            if 'nextExcel' in self.configs.keys():
                self.excelPath = self.configs['nextExcel']
        pass

    def closeWindow(self):
        if len(self.dbProcList) > 0 or len(self.serverProcList) > 0:
            SystemUtils.killProcess(self.serverProcList + self.dbProcList)
            SystemUtils.killAllProcess()
        self.root.quit()
        pass


def main():
    tool = SvnTool()
    tool.elementArrange()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
