#!/usr/bin/python
# coding=UTF8
from xml.dom.minidom import parse
import xml.dom.minidom


def getDictFromXML():
    configs = {}
    domTree = xml.dom.minidom.parse('Configs.xml')

    # <editor-fold desc="Trunk path">
    if domTree.documentElement.getElementsByTagName('trunkServer1'):
        trunkServer1 = domTree.documentElement.getElementsByTagName('trunkServer1')[0]
        if trunkServer1.childNodes:
            configs['trunkServer1'] = trunkServer1.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('trunkServer2'):
        trunkServer2 = domTree.documentElement.getElementsByTagName('trunkServer2')[0]
        if trunkServer2.childNodes:
            configs['trunkServer2'] = trunkServer2.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('trunkClient'):
        trunkClient = domTree.documentElement.getElementsByTagName('trunkClient')[0]
        if trunkClient.childNodes:
            configs['trunkClient'] = trunkClient.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('trunkConfig'):
        trunkConfig = domTree.documentElement.getElementsByTagName('trunkConfig')[0]
        if trunkConfig.childNodes:
            configs['trunkConfig'] = trunkConfig.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('trunkExcel'):
        trunkExcel = domTree.documentElement.getElementsByTagName('trunkExcel')[0]
        if trunkExcel.childNodes:
            configs['trunkExcel'] = trunkExcel.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('trunkText'):
        trunkText = domTree.documentElement.getElementsByTagName('trunkText')[0]
        if trunkText.childNodes:
            configs['trunkText'] = trunkText.childNodes[0].data
    # </editor-fold>

    # <editor-fold desc="Current path">
    if domTree.documentElement.getElementsByTagName('currentServer1'):
        currentServer1 = domTree.documentElement.getElementsByTagName('currentServer1')[0]
        if currentServer1.childNodes:
            configs['currentServer1'] = currentServer1.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('currentServer2'):
        currentServer2 = domTree.documentElement.getElementsByTagName('currentServer2')[0]
        if currentServer2.childNodes:
            configs['currentServer2'] = currentServer2.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('currentClient'):
        currentClient = domTree.documentElement.getElementsByTagName('currentClient')[0]
        if currentClient.childNodes:
            configs['currentClient'] = currentClient.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('currentConfig'):
        currentConfig = domTree.documentElement.getElementsByTagName('currentConfig')[0]
        if currentConfig.childNodes:
            configs['currentConfig'] = currentConfig.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('currentExcel'):
        currentExcel = domTree.documentElement.getElementsByTagName('currentExcel')[0]
        if currentExcel.childNodes:
            configs['currentExcel'] = currentExcel.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('currentText'):
        currentText = domTree.documentElement.getElementsByTagName('currentText')[0]
        if currentText.childNodes:
            configs['currentText'] = currentText.childNodes[0].data
    # </editor-fold>

    # <editor-fold desc="Next path">
    if domTree.documentElement.getElementsByTagName('nextServer1'):
        nextServer1 = domTree.documentElement.getElementsByTagName('nextServer1')[0]
        if nextServer1.childNodes[0]:
            configs['nextServer1'] = nextServer1.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('nextServer2'):
        nextServer2 = domTree.documentElement.getElementsByTagName('nextServer2')[0]
        if nextServer2.childNodes:
            configs['nextServer2'] = nextServer2.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('nextClient'):
        nextClient = domTree.documentElement.getElementsByTagName('nextClient')[0]
        if nextClient.childNodes:
            configs['nextClient'] = nextClient.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('nextConfig'):
        nextConfig = domTree.documentElement.getElementsByTagName('nextConfig')[0]
        if nextConfig.childNodes:
            configs['nextConfig'] = nextConfig.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('nextExcel'):
        nextExcel = domTree.documentElement.getElementsByTagName('nextExcel')[0]
        if nextExcel.childNodes:
            configs['nextExcel'] = nextExcel.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('nextText'):
        nextText = domTree.documentElement.getElementsByTagName('nextText')[0]
        if nextText.childNodes:
            configs['nextText'] = nextText.childNodes[0].data
    # </editor-fold>

    return configs
