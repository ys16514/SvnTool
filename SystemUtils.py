import psutil
import os, signal


def killServerProcess():
    pids = psutil.pids()
    for pid in pids:
        try:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)
                if p and p.name() == 'node.exe':
                    os.kill(pid, signal.SIGINT)
        except psutil.NoSuchProcess:
            pass


def killDbProcess():
    pids = psutil.pids()
    for pid in pids:
        try:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)
                if p and p.name() == 'redis-server.exe':
                    os.kill(pid, signal.SIGINT)
        except psutil.NoSuchProcess:
            pass


def killAllProcess():
    pids = psutil.pids()
    for pid in pids:
        try:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)
                if p:
                    if p.name() == 'redis-server.exe' or p.name() == 'node.exe':
                        os.kill(pid, signal.SIGINT)
        except psutil.NoSuchProcess:
            pass
