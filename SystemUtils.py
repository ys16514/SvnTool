import psutil
import time
from datetime import datetime


def saveToLog(infoStr):
    with open('error.log', 'a') as f:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(str(now) + ' ' + infoStr + '\n')
        f.close()


def isDBOpen(ports):
    pids = psutil.pids()
    portsList = []
    result = False
    for pid in pids:
        try:
            if psutil.pid_exists(pid):
                p = psutil.Process(pid)
                if p and p.name() == 'redis-server.exe':
                    portsList.append(p.connections()[0].laddr.port)
        except psutil.NoSuchProcess:
            continue
    if len(portsList) >= len(ports):
        cnt = 0
        for port in ports:
            if port in portsList:
                cnt = cnt + 1
        if cnt == len(ports):
            result = True
    return result


def killProcess(procList):
    if isinstance(procList, list):
        if len(procList) > 0:
            for proc in procList:
                proc.kill()


def getDateFromStamp(timeStamp):
    try:
        timeStamp = int(timeStamp)
        if len(str(timeStamp)) == 10:
            time_local = time.localtime(timeStamp)
        elif len(str(timeStamp)) == 13:
            time_local = time.localtime(int(timeStamp / 1000))
        else:
            raise Exception('Time Stamp Error', 'Invalid time stamp')
        return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    except Exception:
        raise Exception('Time Stamp Error', 'Invalid time stamp')

# def killServerProcess():
#     pids = psutil.pids()
#     for pid in pids:
#         try:
#             if psutil.pid_exists(pid):
#                 p = psutil.Process(pid)
#                 if p and p.name() == 'node.exe':
#                     p.terminate()
#         except psutil.NoSuchProcess as e:
#             infoDict = {}
#             infoDict['pids'] = pids
#             infoDict['pid'] = pid
#             infoDict['pidName'] = psutil.Process(pid).name()
#             infoDict['error'] = e
#             saveToLog(str(infoDict))
#             continue


# def killDbProcess():
#     pids = psutil.pids()
#     for pid in pids:
#         try:
#             if psutil.pid_exists(pid):
#                 p = psutil.Process(pid)
#                 if p and p.name() == 'redis-server.exe':
#                     p.terminate()
#         except psutil.AccessDenied:
#             infoDict = {}
#             infoDict['pids'] = pids
#             infoDict['pid'] = pid
#             infoDict['pidName'] = psutil.Process(pid).name()
#             saveToLog(str(infoDict))
#             continue


# def killAllProcess():
#     pids = psutil.pids()
#     for pid in pids:
#         try:
#             if psutil.pid_exists(pid):
#                 p = psutil.Process(pid)
#                 if p:
#                     if p.name() == 'redis-server.exe' or p.name() == 'node.exe':
#                         p.terminate()
#         except psutil.NoSuchProcess as e:
#             infoDict = {}
#             infoDict['pids'] = pids
#             infoDict['pid'] = pid
#             infoDict['pidName'] = psutil.Process(pid).name()
#             infoDict['error'] = e
#             saveToLog(str(infoDict))
#             continue

# def isDate(year, month, day):
#     result = True
#     try:
#         date = datetime.strptime(str(year) + '-' + str(month) + '-' + str(day) + '-' + \
#                                  '00:00:00',
#                                  "%Y-%m-%d-%H:%M:%S")
#     except Exception as e:
#         result = False
#     return result
#
#
# def isTime(hour, minute, second):
#     result = True
#     try:
#         time = datetime.strptime('2018-11-30' + \
#                                  str(hour) + ':' + str(minute) + ':' + str(second),
#                                  "%Y-%m-%d-%H:%M:%S")
#     except Exception as e:
#         result = False
#     return result
#
#
# def changeDate(year, month, day):
#     if isDate(year, month, day):
#         os.system("date %d.%d.%d" % (year, month, day))
#
#
# def changeTime(hour, minute, second):
#     if isTime(hour, minute, second):
#         os.system("time %d.%d.%d" % (hour, minute, second))
