import psutil
import os, signal


def killProcess():
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == 'redis-server.exe' or p.name() == 'node.exe':
            os.kill(pid, signal.SIGINT)
