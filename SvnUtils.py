#!/usr/bin/python
# coding=UTF8
import os

dirChange = 'cd svnDir'
exePath = 'svn.exe'


def update(assetPath, excelPath, serverPaths, doUpdate=False):
    pathExist = True
    for path in serverPaths:
        if not os.path.exists(path):
            pathExist = False
            break
    if os.path.exists(assetPath) and os.path.exists(excelPath) and pathExist:
        if (doUpdate):
            command = dirChange + ' && ' + \
                      exePath + " update " + '"' + assetPath + '\\"' + ' && ' + \
                      exePath + " update " + '"' + excelPath + '\\"' + ' && '
            for path in serverPaths:
                command = command + exePath + " update " + '"' + path + '\\"' + ' && '
            command = command + ' pause'
            if not os.system(command) == 0:
                raise Exception("Svn Error!", "error in svn update")
    else:
        err = 'The path not exist'
        raise Exception("Path Error!", err)


def revert(assetPath, excelPath, serverPaths, doRevert=False):
    pathExist = True
    for path in serverPaths:
        if not os.path.exists(path):
            pathExist = False
            break
    if os.path.exists(assetPath) and os.path.exists(excelPath) and pathExist:
        if (doRevert):
            command = dirChange + ' && ' + \
                      exePath + " revert -R " + '"' + assetPath + '\\"' + ' && ' + \
                      exePath + " revert -R " + '"' + excelPath + '\\"' + ' && '
            for path in serverPaths:
                command = command + exePath + " revert -R " + '"' + path + '\\"' + ' && '
            command = command + ' pause'
            if not os.system(command) == 0:
                raise Exception("Svn Error!", "error in svn revert")
    else:
        err = 'The path not exist'
        raise Exception("Path Error!", err)
