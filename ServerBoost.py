import os

redisCommand = "redis-server.exe redis.conf --maxheap 200m"
funcCommand = "node gas_func"
matchCommand = "node gas_match"
chatCommand = "node gas_chat"
toolCommand = "node gas_tool"

redisPath = 'db\\'
funcPath = 'func_server\\'
chatPath = 'chat_server\\'
toolPath = 'tool_server\\'


def run(command):
    if not os.system(command) == 0:
        raise Exception("ServerBoost Error!", "error in %s" % command)


def serverBoost(serverPath):
    disk = serverPath.split('\\')[0]

    redisCmd = disk + " && " + "cd " + serverPath + redisPath + " && " + redisCommand
    run(redisCmd)
    # print(redisCmd)

    funcCmd = disk + " && " + "cd " + serverPath + funcPath + " && " + funcCommand
    run(funcCmd)
    # print(funcCmd)

    matchCmd = disk + " && " + "cd " + serverPath + funcPath + " && " + matchCommand
    run(matchCmd)
    # print(matchCmd)

    chatCmd = disk + " && " + "cd " + serverPath + chatPath + " && " + chatCommand
    run(chatCmd)
    # print(chatCmd)

    toolCmd = disk + " && " + "cd " + serverPath + toolPath + " && " + toolCommand
    run(toolCmd)
    # print(toolCmd)
