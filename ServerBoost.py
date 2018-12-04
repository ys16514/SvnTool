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


def run(command):
    subprocess.Popen(command)


def localFlush(serverPaths):
    localPath = os.getcwd()

    ports = []
    serverList = []

    if len(serverPaths) > 0 and os.path.exists(serverPaths[0]):

        os.chdir(serverPaths[0] + funcPath)
        with open('GameConfig.json', 'rb') as f:
            gameConfig = json.load(f)

        if 'server_list' in gameConfig.keys():
            serverList = gameConfig['server_list']

        # 获取 Redis 端口号
        for server in serverList:
            ports.append(server['redis_port'])

        if not SystemUtils.isDBOpen(ports):
            os.chdir(localPath)
            raise Exception("Redis Error!", "Redis ports do not match")
        else:
            if len(serverPaths) == len(ports):
                for index in range(len(serverPaths)):
                    os.chdir(serverPaths[index] + redisPath)
                    os.system('redis-cli -p %s -a fb123456 flushall' % ports[index])

    # 工作路径还原
    os.chdir(localPath)


def redisBoost(serverPaths):
    localPath = os.getcwd()

    if len(serverPaths) > 0:
        for path in serverPaths:
            if os.path.exists(path):
                # 启动 Redis
                os.chdir(path + redisPath)
                run(redisCommand)

                time.sleep(1)

    # 工作路径还原
    os.chdir(localPath)


def serverBoost(serverPaths):
    localPath = os.getcwd()

    if len(serverPaths) > 0:
        for path in serverPaths:
            if os.path.exists(path):
                os.chdir(path + funcPath)
                run(funcCommand)

                os.chdir(path + funcPath)
                run(matchCommand)

                os.chdir(path + chatPath)
                run(chatCommand)

                time.sleep(4)

        # 启动 GM
        if os.path.exists(serverPaths[0]):
            os.chdir(serverPaths[0] + toolPath)
            run(toolCommand)

    # 工作路径还原
    os.chdir(localPath)
