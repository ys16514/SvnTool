#!/usr/bin/python
# coding=UTF8
import os
import sys
import XMLParse


def cmd(path, doUpdate=False, doRevert=False):
    # svn revert 操作
    if (doRevert):
        try:
            print("Start reverting " + path)
            cmd = "svn revert -R " + path
            if not os.system(cmd) == 0:
                print("error in svn revert.")
                sys.exit(1)
        except Exception as e:
            print("error occurs in svnUpdate: " + str(e))
            sys.exit(1)

    # svn update 操作
    if (doUpdate):
        try:
            print("Start updating " + path)
            cmd = "svn update " + path
            if not os.system(cmd) == 0:
                print("error in svn update.")
                sys.exit(1)

        except Exception as e:
            print("error occurs in svnUpdate: " + str(e))
            sys.exit(1)


def update(path, doUpdate=False, doRevert=False):
    if os.path.exists(path):
        cmd('"' + path + '"', doUpdate, doRevert)
    else:
        print('The path of %s not exist' % path)


if __name__ == '__main__':

    configs = XMLParse.getDictFromXML()

    # 变量初始化
    doRevert = False
    assetPath = ''
    excelPath = ''
    serverPath_1 = ''
    serverPath_2 = ''
    version = input("Please input the version (trunk(1) / current(2) / next(3)): ")
    revert = input("Revert or not (yes(1) / no(2)): ")

    # 根据分支版本确定svn更新路径
    if version == '1':
        if 'trunkClient' in configs.keys():
            assetPath = configs['trunkClient']
        if 'trunkExcel' in configs.keys():
            excelPath = configs['trunkExcel']
        if 'trunkServer1' in configs.keys():
            serverPath_1 = configs['trunkServer1']
        if 'trunkServer2' in configs.keys():
            serverPath_2 = configs['trunkServer2']
    elif version == '2':
        if 'currentClient' in configs.keys():
            assetPath = configs['currentClient']
        if 'currentExcel' in configs.keys():
            excelPath = configs['currentExcel']
        if 'currentServer1' in configs.keys():
            serverPath_1 = configs['currentServer1']
        if 'currentServer2' in configs.keys():
            serverPath_2 = configs['currentServer2']
    elif version == '3':
        if 'nextClient' in configs.keys():
            assetPath = configs['nextClient']
        if 'nextExcel' in configs.keys():
            excelPath = configs['nextExcel']
        if 'nextServer1' in configs.keys():
            serverPath_1 = configs['nextServer1']
        if 'nextServer2' in configs.keys():
            serverPath_2 = configs['nextServer2']

    # 确定svn更新前是否revert本地操作
    if revert == '1':
        doRevert = True

    # 更新 Asset
    update(assetPath, doRevert, True)

    # 更新 Excel
    update(excelPath, doRevert, True)

    # 更新 Server_1
    update(serverPath_1, doRevert, True)

    # 更新 Server_2
    update(serverPath_2, doRevert, True)

    # 更新结束提示
    input("Update finished......")
