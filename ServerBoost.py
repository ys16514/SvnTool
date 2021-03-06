#!/usr/bin/python
# coding=UTF8
import os
import subprocess
from json import load
from time import sleep
import SystemUtils

redisCommand = "redis-server.exe redis.conf --maxheap 200m"
funcCommand = "node gas_func"
matchCommand = "node gas_match"
chatCommand = "node gas_chat"
toolCommand = "node gas_tool"

redisPath = 'db\\'
funcPath = 'func_server\\'
chatPath = 'chat_server\\'
toolPath = 'gm_tool_server\\'

LOCALPATH = os.getcwd()


def run(command, isHide=False):
    try:
        if isHide:
            if command in [redisCommand, funcCommand]:
                return subprocess.Popen(command)
            else:
                return subprocess.Popen(command,
                                        shell=True,
                                        stdin=subprocess.DEVNULL,
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL)
        else:
            return subprocess.Popen(command)
    except Exception as e:
        raise Exception("Cmd Error!", "Error in %s : %s" % (command, str(e)))


def getPortsFromPaths(serverPaths):
    localPath = os.getcwd()

    ports = []
    serverList = []

    try:
        if len(serverPaths) > 0 and os.path.exists(serverPaths[0]):

            os.chdir(serverPaths[0] + funcPath)
            with open('GameConfig.json', 'rb') as f:
                gameConfig = load(f)

            if 'server_list' in gameConfig.keys():
                serverList = gameConfig['server_list']

            # 获取 Redis 端口号
            for server in serverList:
                ports.append(server['redis_port'])
    except Exception as e:
        os.chdir(localPath)
        raise Exception("Config Error!", "无法获取端口参数 : %s" % str(e))

    os.chdir(localPath)

    return ports


def localFlush(serverPaths):
    localPath = os.getcwd()

    ports = getPortsFromPaths(serverPaths)

    try:
        if len(ports) > 0:
            if len(serverPaths) == len(ports):
                for index in range(len(serverPaths)):
                    os.chdir(serverPaths[index] + redisPath)
                    if not os.system('redis-cli -p %s -a fb123456 flushall' % ports[index]) == 0:
                        raise Exception("Cmd Error!", "缺少 redis-cli.exe 文件 或者 端口错误")
        else:
            os.chdir(localPath)
            raise Exception("Config Error!", "缺少端口参数")

    except Exception as e:
        os.chdir(localPath)
        raise Exception("Redis Error!", "Error in localFlush() : %s" % str(e))

    # 工作路径还原
    os.chdir(localPath)


def redisBoost(serverPaths):
    localPath = os.getcwd()
    procList = []
    try:
        if len(serverPaths) > 0:
            for path in serverPaths:
                if os.path.exists(path):
                    # 启动 Redis
                    os.chdir(path + redisPath)
                    procList.append(run(redisCommand))

                    sleep(1)
    except Exception as e:
        os.chdir(localPath)
        raise Exception("Redis Error!", "Error in redisBoost() : %s" % str(e))

    # 工作路径还原
    os.chdir(localPath)
    return procList


def serverBoost(serverPaths, isHide):
    localPath = os.getcwd()
    procList = []
    try:
        if len(serverPaths) > 0:
            for path in serverPaths:
                if os.path.exists(path):
                    os.chdir(path + funcPath)
                    procList.append(run(funcCommand, isHide))

                    os.chdir(path + funcPath)
                    procList.append(run(matchCommand, isHide))

                    os.chdir(path + chatPath)
                    procList.append(run(chatCommand, isHide))

                    sleep(5)

            # 启动 GM
            if os.path.exists(serverPaths[0]):
                os.chdir(serverPaths[0] + toolPath)
                procList.append(run(toolCommand, isHide))

    except Exception as e:
        os.chdir(localPath)
        raise Exception("Server Error!", "Error in serverBoost() : %s" % str(e))

    # 工作路径还原
    os.chdir(localPath)
    return procList
