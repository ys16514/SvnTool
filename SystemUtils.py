import psutil
import os, signal
from datetime import datetime


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


def isDate(year, month, day):
    result = True
    try:
        date = datetime.strptime(str(year) + '-' + str(month) + '-' + str(day) + '-' + \
                                 '00:00:00',
                                 "%Y-%m-%d-%H:%M:%S")
    except Exception as e:
        result = False
    return result


def isTime(hour, minute, second):
    result = True
    try:
        time = datetime.strptime('2018-11-30' + \
                                 str(hour) + ':' + str(minute) + ':' + str(second),
                                 "%Y-%m-%d-%H:%M:%S")
    except Exception as e:
        result = False
    return result


def changeDate(year, month, day):
    if isDate(year, month, day):
        os.system("date %d.%d.%d" % (year, month, day))


def changeTime(hour, minute, second):
    if isTime(hour, minute, second):
        os.system("time %d.%d.%d" % (hour, minute, second))
