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

    if domTree.documentElement.getElementsByTagName('trunkAsset'):
        trunkAsset = domTree.documentElement.getElementsByTagName('trunkAsset')[0]
        if trunkAsset.childNodes:
            configs['trunkAsset'] = trunkAsset.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('trunkExcel'):
        trunkExcel = domTree.documentElement.getElementsByTagName('trunkExcel')[0]
        if trunkExcel.childNodes:
            configs['trunkExcel'] = trunkExcel.childNodes[0].data
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

    if domTree.documentElement.getElementsByTagName('currentAsset'):
        currentAsset = domTree.documentElement.getElementsByTagName('currentAsset')[0]
        if currentAsset.childNodes:
            configs['currentAsset'] = currentAsset.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('currentExcel'):
        currentExcel = domTree.documentElement.getElementsByTagName('currentExcel')[0]
        if currentExcel.childNodes:
            configs['currentExcel'] = currentExcel.childNodes[0].data
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

    if domTree.documentElement.getElementsByTagName('nextAsset'):
        nextAsset = domTree.documentElement.getElementsByTagName('nextAsset')[0]
        if nextAsset.childNodes:
            configs['nextAsset'] = nextAsset.childNodes[0].data

    if domTree.documentElement.getElementsByTagName('nextExcel'):
        nextExcel = domTree.documentElement.getElementsByTagName('nextExcel')[0]
        if nextExcel.childNodes:
            configs['nextExcel'] = nextExcel.childNodes[0].data
    # </editor-fold>

    return configs
