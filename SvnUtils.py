#!/usr/bin/python
# coding=UTF8
import os
import subprocess

dirChange = 'cd svnDir'
exePath = 'svn.exe'


def update(assetPath, excelPath, serverPaths, doUpdate=False):
    pathExist = True
    for path in serverPaths:
        if not os.path.exists(path):
            pathExist = False
            break
    if os.path.exists(assetPath) or os.path.exists(excelPath) or pathExist:
        if (doUpdate):
            command = dirChange + ' && '
            if os.path.exists(assetPath):
                command = command + exePath + " update " + '"' + assetPath + '\\"' + ' && '
            if os.path.exists(excelPath):
                command = command + exePath + " update " + '"' + excelPath + '\\"' + ' && '
            if pathExist:
                for path in serverPaths:
                    command = command + exePath + " update " + '"' + path + '\\"' + ' && '
            command = command + ' pause'

            returnCode = os.system(command)
            # 手动关闭cmd，返回值为负数
            # 异常退出，返回值为 1
            if returnCode == 1:
                stdout, stderr = subprocess.Popen(command,
                                                  shell=True,
                                                  stdin=subprocess.DEVNULL,
                                                  stdout=subprocess.DEVNULL,
                                                  stderr=subprocess.PIPE).communicate()
                if stderr:
                    errInfo = stderr.decode('gbk').strip()
                    if errInfo != '':
                        raise Exception("Svn Error!", "error in svn update: %s" % errInfo)
    else:
        err = 'The path not exist'
        raise Exception("Path Error!", err)


def revert(assetPath, excelPath, serverPaths, doRevert=False):
    pathExist = True
    for path in serverPaths:
        if not os.path.exists(path):
            pathExist = False
            break
    if os.path.exists(assetPath) or os.path.exists(excelPath) or pathExist:
        if (doRevert):
            command = dirChange + ' && '
            if os.path.exists(assetPath):
                command = command + exePath + " revert -R " + '"' + assetPath + '\\"' + ' && '
            if os.path.exists(excelPath):
                command = command + exePath + " revert -R " + '"' + excelPath + '\\"' + ' && '
            if pathExist:
                for path in serverPaths:
                    command = command + exePath + " revert -R " + '"' + path + '\\"' + ' && '
            command = command + ' pause'

            returnCode = os.system(command)
            if returnCode == 1:
                stdout, stderr = subprocess.Popen(command,
                                                  shell=True,
                                                  stdin=subprocess.DEVNULL,
                                                  stdout=subprocess.DEVNULL,
                                                  stderr=subprocess.PIPE).communicate()
                if stderr:
                    errInfo = stderr.decode('gbk').strip()
                    if errInfo != '':
                        raise Exception("Svn Error!", "error in svn revert: %s" % errInfo)
    else:
        err = 'The path not exist'
        raise Exception("Path Error!", err)
