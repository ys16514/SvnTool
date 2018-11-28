import psutil
import os, signal


def killServerProcess():
    pids = psutil.pids()
    for pid in pids:
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            if p and p.name() == 'node.exe':
                os.kill(pid, signal.SIGINT)

def killDbProcess():
    pids = psutil.pids()
    for pid in pids:
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            if p and p.name() == 'redis-server.exe':
                os.kill(pid, signal.SIGINT)

def killAllProcess():
    pids = psutil.pids()
    for pid in pids:
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            if p and p.name() == 'redis-server.exe' or p.name() == 'node.exe':
                os.kill(pid, signal.SIGINT)
