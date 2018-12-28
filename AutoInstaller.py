import os
import shutil

cmd = "pyinstaller -F -w Main.py"
if os.path.exists("E:\Codes\Python\SvnTool\dist"):
    shutil.rmtree("E:\Codes\Python\SvnTool\dist")
if os.path.exists("E:\Codes\Python\SvnTool\\build"):
    shutil.rmtree("E:\Codes\Python\SvnTool\\build")
if os.path.exists("E:\Codes\Python\SvnTool\\Main.spec"):
    os.remove("E:\Codes\Python\SvnTool\\Main.spec")
if os.system(cmd) == 0:
    if os.path.exists("E:\SvnTool V2.0\Main.exe"):
        os.remove("E:\SvnTool V2.0\Main.exe")
    shutil.copyfile("dist\Main.exe", "E:\SvnTool V2.0\Main.exe")
