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
        self.root = tkinter.Tk()
        self.root.title("SvnTool")
        self.root.geometry('380x140')
        self.version = tkinter.IntVar()
        self.configs = {}
        self.serverPaths = []
        self.assetPath = ''
        self.excelPath = ''
        self.currentBranch = 0
        self.nextBranch = 0

        # 选择分支的三个选项
        self.choice1 = tkinter.Radiobutton(self.root, text="主干", variable=self.version, value=1)
        self.choice2 = tkinter.Radiobutton(self.root, text="线上分支", variable=self.version, value=2)
        self.choice3 = tkinter.Radiobutton(self.root, text="提审分支", variable=self.version, value=3)

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

    def updateCall(self):
        try:
            if self.version.get() == 1:
                self.update(1)
            elif self.version.get() == 2:
                self.update(2)
            elif self.version.get() == 3:
                self.update(3)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def revertCall(self):
        try:
            # if self.version.get() == 1:
            #     self.revert(1)
            # elif self.version.get() == 2:
            #     self.revert(2)
            # elif self.version.get() == 3:
            #     self.revert(3)
            # else:
            messagebox.showwarning("Warning", "请手动回退")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def boostCall(self):
        try:
            if self.version.get() == 1:
                self.boost(1)
            elif self.version.get() == 2:
                self.boost(2)
            elif self.version.get() == 3:
                self.boost(3)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def flushCall(self):
        try:
            self.nextBranch = self.version.get()
            if self.currentBranch != 0 and self.currentBranch != self.nextBranch:
                messagebox.showwarning("Warning", "请确保Branch相同")
            else:
                self.currentBranch = self.nextBranch
                if self.version.get() == 1:
                    flag = messagebox.askyesno("Warning", "确定清档吗？")
                    if flag:
                        self.flush(1)
                elif self.version.get() == 2:
                    flag = messagebox.askyesno("Warning", "确定清档吗？")
                    if flag:
                        self.flush(2)
                elif self.version.get() == 3:
                    flag = messagebox.askyesno("Warning", "确定清档吗？")
                    if flag:
                        self.flush(3)
                else:
                    messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def shutCall(self):
        self.currentBranch = 0
        try:
            if self.version.get() == 1:
                SystemUtils.killAllProcess()
            elif self.version.get() == 2:
                SystemUtils.killAllProcess()
            elif self.version.get() == 3:
                SystemUtils.killAllProcess()
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def redisCall(self):
        try:
            self.currentBranch = self.version.get()
            if self.version.get() == 1:
                SystemUtils.killDbProcess()
                self.redisBoost(1)
            elif self.version.get() == 2:
                SystemUtils.killDbProcess()
                self.redisBoost(2)
            elif self.version.get() == 3:
                SystemUtils.killDbProcess()
                self.redisBoost(3)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update(self, version):
        self.getPathFromXML(version)
        SvnUtils.update(self.assetPath, self.excelPath, self.serverPaths, True)

    def revert(self, version):
        flag = messagebox.askyesno("Warning", "确定回退本地的所有修改吗？")
        if flag:
            self.getPathFromXML(version)
            SvnUtils.revert(self.assetPath, self.excelPath, self.serverPaths, True)

    def boost(self, version):
        self.getPathFromXML(version)
        ports = ServerBoost.getPortsFromPaths(self.serverPaths)
        if not SystemUtils.isDBOpen(ports):
            messagebox.showwarning("Warning", "请先启动DB！")
        else:
            SystemUtils.killServerProcess()
            ServerBoost.serverBoost(self.serverPaths)

    def flush(self, version):
        self.getPathFromXML(version)
        ports = ServerBoost.getPortsFromPaths(self.serverPaths)
        if not SystemUtils.isDBOpen(ports):
            messagebox.showwarning("Warning", "请先启动DB！")
        else:
            ServerBoost.localFlush(self.serverPaths)
            messagebox.showinfo("Done", "清档成功")

    def redisBoost(self, version):
        self.getPathFromXML(version)
        ServerBoost.redisBoost(self.serverPaths)

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


def main():
    tool = SvnTool()
    tool.elementArrange()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
