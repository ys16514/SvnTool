#!/usr/bin/python
# coding=UTF8
import os

dirChange = 'cd svnDir'
exePath = 'svn.exe'


def update(assetPath, excelPath, server1Path, server2Path, doUpdate=False):
    if os.path.exists(assetPath) and os.path.exists(excelPath) and os.path.exists(server1Path) and os.path.exists(server2Path):
        if (doUpdate):
            command = dirChange + ' && ' +\
                      exePath + " update " + '"' + assetPath + '\\"' + ' && ' +\
                      exePath + " update " + '"' + excelPath + '\\"' + ' && ' + \
                      exePath + " update " + '"' + server1Path + '\\"' + ' && ' + \
                      exePath + " update " + '"' + server2Path + '\\"' + ' && pause'
            if not os.system(command) == 0:
                raise Exception("Svn Error!", "error in svn update")
    else:
        err = 'The path not exist'
        raise Exception("Path Error!", err)


def revert(assetPath, excelPath, server1Path, server2Path, doRevert=False):
    if os.path.exists(assetPath) and os.path.exists(excelPath) and os.path.exists(server1Path) and os.path.exists(server2Path):
        if (doRevert):
            command = dirChange + ' && ' +\
                      exePath + " revert -R " + '"' + assetPath + '\\"' + ' && ' +\
                      exePath + " revert -R " + '"' + excelPath + '\\"' + ' && ' + \
                      exePath + " revert -R " + '"' + server1Path + '\\"' + ' && ' + \
                      exePath + " revert -R " + '"' + server2Path + '\\"' + ' && pause'
            if not os.system(command) == 0:
                raise Exception("Svn Error!", "error in svn revert")
    else:
        err = 'The path not exist'
        raise Exception("Path Error!", err)
