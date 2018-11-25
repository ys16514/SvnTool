#!/usr/bin/python
# coding=UTF8
import os

exePath = 'svn'


def update(originPath, doUpdate=False):
    if os.path.exists(originPath):
        if (doUpdate):
            path = '"' + originPath + '"'
            command = exePath + " update " + path
            if not os.system(command) == 0:
                raise Exception("Svn Error!", "error in svn update")
    else:
        err = 'The path of %s not exist' % originPath
        raise Exception("Path Error!", err)


def revert(originPath, doRevert=False):
    if os.path.exists(originPath):
        if (doRevert):
            path = '"' + originPath + '"'
            command = exePath + " revert -R " + path
            if not os.system(command) == 0:
                raise Exception("Svn Error!", "error in svn revert")
    else:
        err = 'The path of %s not exist' % originPath
        raise Exception("Path Error!", err)
