import os
import subprocess

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


def serverBoost(server1Path, server2Path):
    localPath = os.getcwd()

    os.chdir(server1Path + redisPath)
    run(redisCommand)

    if server2Path != '':
        os.chdir(server2Path + redisPath)
        run(redisCommand)

    os.chdir(server1Path + funcPath)
    run(funcCommand)

    os.chdir(server1Path + funcPath)
    run(matchCommand)

    os.chdir(server1Path + chatPath)
    run(chatCommand)

    os.chdir(server1Path + toolPath)
    run(toolCommand)

    os.chdir(localPath)
