#!/usr/bin/python
# coding=UTF8
import tkinter
from tkinter import messagebox
from tkinter import ttk
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
        # self.year = tkinter.IntVar()
        # self.month = tkinter.IntVar()
        # self.day = tkinter.IntVar()
        self.configs = {}
        self.serverPaths = []
        self.assetPath = ''
        self.excelPath = ''

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
        # # 穿越按钮
        # self.timeButton = tkinter.Button(self.root, text="穿越", command=self.timeCall)
        # # 年份下拉列表
        # self.yearCombo = ttk.Combobox(self.root, textvariable=self.year)
        # self.yearCombo['value'] = tuple(range(2018, 2101))
        # self.yearCombo.current(0)
        # # 月份下拉列表
        # self.monthCombo = ttk.Combobox(self.root, textvariable=self.month)
        # self.monthCombo['value'] = tuple(range(1, 13))
        # self.monthCombo.current(0)
        # # 天数下拉列表
        # self.dayCombo = ttk.Combobox(self.root, textvariable=self.day)
        # self.dayCombo['value'] = tuple(range(1, 32))
        # self.dayCombo.current(0)
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
        # self.yearCombo.grid(row=4, column=1)
        # self.monthCombo.grid(row=5, column=1)
        # self.dayCombo.grid(row=6, column=1)
        # self.timeButton.grid(row=7, column=1)

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
            if self.version.get() == 1:
                self.revert(1)
            elif self.version.get() == 2:
                self.revert(2)
            elif self.version.get() == 3:
                self.revert(3)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def boostCall(self):
        try:
            SystemUtils.killServerProcess()
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
        flag = messagebox.askyesno("Warning", "确定清档吗？")
        if flag:
            try:
                if self.version.get() == 1:
                    self.flush(1)
                    messagebox.showinfo("Done", "清档成功")
                elif self.version.get() == 2:
                    self.flush(2)
                    messagebox.showinfo("Done", "清档成功")
                elif self.version.get() == 3:
                    self.flush(3)
                    messagebox.showinfo("Done", "清档成功")
                else:
                    messagebox.showwarning("Warning", "请先选择一个Branch！")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def shutCall(self):
        SystemUtils.killAllProcess()

    def redisCall(self):
        try:
            SystemUtils.killDbProcess()
            if self.version.get() == 1:
                self.redisBoost(1)
            elif self.version.get() == 2:
                self.redisBoost(2)
            elif self.version.get() == 3:
                self.redisBoost(3)
            else:
                messagebox.showwarning("Warning", "请先选择一个Branch！")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # def timeCall(self):
    #     try:
    #         SystemUtils.changeDate(self.year.get(), self.month.get(), self.day.get())
    #     except Exception as e:
    #         messagebox.showerror("Error", str(e))

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
        ServerBoost.serverBoost(self.serverPaths)

    def flush(self, version):
        self.getPathFromXML(version)
        ServerBoost.localFlush(self.serverPaths)

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
