#!/usr/bin/python
# coding=UTF8
import tkinter
from tkinter import messagebox
import SvnUtils
import XMLParse
import ServerBoost


class SvnTool(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("SvnTool")
        self.root.geometry('200x120')
        self.version = tkinter.IntVar()
        self.configs = {}
        self.assetPath = ''
        self.excelPath = ''
        self.server1Path = ''
        self.server2Path = ''

        # 选择分支的三个选项
        self.choice1 = tkinter.Radiobutton(self.root, text="主干", variable=self.version, value=1)
        self.choice2 = tkinter.Radiobutton(self.root, text="线上分支", variable=self.version, value=2)
        self.choice3 = tkinter.Radiobutton(self.root, text="提审分支", variable=self.version, value=3)

        # 更新按钮
        self.updateButton = tkinter.Button(self.root, text="Update", command=self.updateCall)
        # 回退按钮
        self.revertButton = tkinter.Button(self.root, text="Revert", command=self.revertCall)
        # 启动按钮
        self.boostButton = tkinter.Button(self.root, text="Boost", command=self.boostCall)
        pass

    def elementArrange(self):
        self.choice1.grid(row=1, column=0, sticky=tkinter.W, padx=10, ipady=8)
        self.choice2.grid(row=2, column=0, sticky=tkinter.W, padx=10, ipady=8)
        self.choice3.grid(row=3, column=0, sticky=tkinter.W, padx=10, ipady=8)
        self.updateButton.grid(row=1, column=2, padx=20)
        self.revertButton.grid(row=2, column=2, padx=20)
        self.boostButton.grid(row=3, column=2, padx=20)

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
        pass

    def update(self, version):
        self.getPathFromXML(version)
        SvnUtils.update(self.assetPath, True)
        SvnUtils.update(self.excelPath, True)
        SvnUtils.update(self.server1Path, True)
        SvnUtils.update(self.server2Path, True)

    def revert(self, version):
        flag = messagebox.askyesno("Warning", "确定回退本地的修改吗？")
        if flag:
            self.getPathFromXML(version)
            SvnUtils.revert(self.assetPath, True)
            SvnUtils.revert(self.excelPath, True)
            SvnUtils.revert(self.server1Path, True)
            SvnUtils.revert(self.server2Path, True)

    def boost(self, version):
        self.getPathFromXML(version)
        ServerBoost.serverBoost(self.server1Path)
        pass

    def getPathFromXML(self, version):
        self.configs = XMLParse.getDictFromXML()

        if version == 1:
            if 'trunkAsset' in self.configs.keys():
                self.assetPath = self.configs['trunkAsset']
            if 'trunkServer1' in self.configs.keys():
                self.server1Path = self.configs['trunkServer1']
            if 'trunkServer2' in self.configs.keys():
                self.server2Path = self.configs['trunkServer2']
            if 'trunkExcel' in self.configs.keys():
                self.excelPath = self.configs['trunkExcel']
        elif version == 2:
            if 'currentAsset' in self.configs.keys():
                self.assetPath = self.configs['currentAsset']
            if 'currentServer1' in self.configs.keys():
                self.server1Path = self.configs['currentServer1']
            if 'currentServer2' in self.configs.keys():
                self.server2Path = self.configs['currentServer2']
            if 'currentExcel' in self.configs.keys():
                self.excelPath = self.configs['currentExcel']
        elif version == 3:
            if 'nextAsset' in self.configs.keys():
                self.assetPath = self.configs['nextAsset']
            if 'nextServer1' in self.configs.keys():
                self.server1Path = self.configs['nextServer1']
            if 'nextServer2' in self.configs.keys():
                self.server2Path = self.configs['nextServer2']
            if 'nextExcel' in self.configs.keys():
                self.excelPath = self.configs['nextExcel']
        pass

    pass


def main():
    tool = SvnTool()
    tool.elementArrange()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
