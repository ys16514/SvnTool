import psutil
import time
from datetime import datetime


# def saveToLog(infoStr):
#     with open('error.log', 'a') as f:
#         now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         f.write(str(now) + ' ' + infoStr + '\n')
#         f.close()


def getDateFromStamp(timeStamp):
    try:
        timeStamp = int(timeStamp)
        if len(str(timeStamp)) == 10:
            time_local = time.localtime(timeStamp)
        elif len(str(timeStamp)) == 13:
            time_local = time.localtime(int(timeStamp / 1000))
        else:
            raise Exception('Time Stamp Error', '无效的时间戳')
        return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    except Exception:
        raise Exception('Time Stamp Error', '无效的时间戳')


def getStampFromDate(date):
    try:
        timeData = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(timeData))
    except Exception:
        raise Exception('Time Data Error', '无效的时间')
    pass


def isDBOpen(ports):
    portsList = []
    result = False
    cnt = 0
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'redis-server.exe':
                portsList.append(proc.connections()[0].laddr.port)
        except Exception:
            continue
    for port in ports:
        if port in portsList:
            cnt = cnt + 1
    if cnt == len(ports) and cnt > 0:
        result = True
    return result


def killProcess(procList):
    if isinstance(procList, list):
        if len(procList) > 0:
            for proc in procList:
                proc.kill()


def killServerProcess():
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'node.exe':
                proc.terminate()
        except Exception:
            continue


def killAllProcess():
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'redis-server.exe' or proc.name() == 'node.exe':
                proc.terminate()
        except Exception:
            continue
