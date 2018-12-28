#!/usr/bin/python
# coding=UTF8
import os
import subprocess
import json
import time
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


def run(command):
    try:
        if command in [redisCommand, funcCommand]:
            return subprocess.Popen(command)
        else:
            return subprocess.Popen(command,
                                    shell=True,
                                    stdin=subprocess.DEVNULL,
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
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
                gameConfig = json.load(f)

            if 'server_list' in gameConfig.keys():
                serverList = gameConfig['server_list']

            # 获取 Redis 端口号
            for server in serverList:
                ports.append(server['redis_port'])
    except Exception as e:
        os.chdir(localPath)
        raise Exception("Config Error!", "Error in getPortsFromPaths() : %s" % str(e))

    os.chdir(localPath)

    return ports


def localFlush(serverPaths):
    localPath = os.getcwd()

    ports = getPortsFromPaths(serverPaths)

    try:

        if len(ports) > 0:
            if not SystemUtils.isDBOpen(ports):
                os.chdir(localPath)
                raise Exception("Redis Error!", "Redis ports do not match")
            else:
                if len(serverPaths) == len(ports):
                    for index in range(len(serverPaths)):
                        os.chdir(serverPaths[index] + redisPath)
                        if not os.system('redis-cli -p %s -a fb123456 flushall' % ports[index]) == 0:
                            raise Exception("Cmd Error!", "error in redis flush")
        else:
            os.chdir(localPath)
            raise Exception("Config Error!", "No Ports Configuration")

    except Exception as e:
        os.chdir(localPath)
        raise Exception("Redis Error!", "Error in localFlush() : %s" % str(e))

    # 工作路径还原
    os.chdir(localPath)


def redisBoost(serverPaths):
    localPath = os.getcwd()

    try:
        if len(serverPaths) > 0:
            for path in serverPaths:
                if os.path.exists(path):
                    # 启动 Redis
                    os.chdir(path + redisPath)
                    run(redisCommand)

                    time.sleep(1)
    except Exception as e:
        os.chdir(localPath)
        raise Exception("Redis Error!", "Error in redisBoost() : %s" % str(e))

    # 工作路径还原
    os.chdir(localPath)


def serverBoost(serverPaths):
    localPath = os.getcwd()
    procList = []
    try:
        if not SystemUtils.isDBOpen(getPortsFromPaths(serverPaths)):
            raise Exception("Redis Error!", "Redis-server is not open")
        else:
            if len(serverPaths) > 0:
                for path in serverPaths:
                    if os.path.exists(path):
                        os.chdir(path + funcPath)
                        procList.append(run(funcCommand))

                        os.chdir(path + funcPath)
                        procList.append(run(matchCommand))

                        os.chdir(path + chatPath)
                        procList.append(run(chatCommand))

                        time.sleep(5)

                # 启动 GM
                if os.path.exists(serverPaths[0]):
                    os.chdir(serverPaths[0] + toolPath)
                    procList.append(run(toolCommand))

    except Exception as e:
        os.chdir(localPath)
        raise Exception("Server Error!", "Error in serverBoost() : %s" % str(e))

    # 工作路径还原
    os.chdir(localPath)
    return procList
