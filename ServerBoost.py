#!/usr/bin/python
# coding=UTF8
import os
import subprocess
import json

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


def localFlush(server1Path, server2Path):
    localPath = os.getcwd()

    port1, port2 = '', ''
    serverList = []

    # 获取 Redis 端口号
    os.chdir(server1Path + funcPath)
    with open('GameConfig.json', 'rb') as f:
        gameConfig = json.load(f)

    if 'server_list' in gameConfig.keys():
        serverList = gameConfig['server_list']
    if len(serverList) == 2:
        port1 = serverList[0]['redis_port']
        port2 = serverList[1]['redis_port']
    if len(serverList) == 1:
        port1 = serverList[0]['redis_port']

    # 1服清档
    os.chdir(server1Path + redisPath)
    os.system('redis-cli -p %s -a fb123456 flushall' % port1)

    # 2服清档
    if port2 != '':
        os.chdir(server2Path + redisPath)
        os.system('redis-cli -p %s -a fb123456 flushall' % port2)

    # 工作路径还原
    os.chdir(localPath)


def redisBoost(server1Path, server2Path):
    localPath = os.getcwd()

    # 启动 1 服 Redis
    os.chdir(server1Path + redisPath)
    run(redisCommand)

    if server2Path != '':
        os.chdir(server2Path + redisPath)
        run(redisCommand)

    # 工作路径还原
    os.chdir(localPath)


def serverBoost(server1Path, server2Path):
    localPath = os.getcwd()

    # 启动 1 服 Redis
    # os.chdir(server1Path + redisPath)
    # run(redisCommand)

    # 启动 2 服 Redis, func, match, chat
    if server2Path != '':
        # os.chdir(server2Path + redisPath)
        # run(redisCommand)

        os.chdir(server2Path + funcPath)
        run(funcCommand)

        os.chdir(server2Path + funcPath)
        run(matchCommand)

        os.chdir(server2Path + chatPath)
        run(chatCommand)

    # 启动 func
    os.chdir(server1Path + funcPath)
    run(funcCommand)

    # 启动 match
    os.chdir(server1Path + funcPath)
    run(matchCommand)

    # 启动 chat
    os.chdir(server1Path + chatPath)
    run(chatCommand)

    # 启动 GM
    os.chdir(server1Path + toolPath)
    run(toolCommand)

    # 工作路径还原
    os.chdir(localPath)
