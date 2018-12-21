#!/usr/bin/python
# coding=UTF8
import xml.etree.ElementTree as ET


def getDictFromXML():
    configs = {}

    tree = ET.ElementTree(file='Configs.xml')

    trunkServerList = []
    currentServerList = []
    nextServerList = []
    for elem1 in tree.iter():

        if elem1.tag == 'redis' and elem1.text is not None:
            configs['redis'] = elem1.text

        if elem1.tag == 'trunkServer':
            for elem2 in elem1.iter():
                if elem2.tag != 'trunkServer' and elem2.text is not None:
                    trunkServerList.append(elem2.text)
        configs['trunkServer'] = trunkServerList
        if elem1.tag == 'trunkAsset' and elem1.text is not None:
            configs['trunkAsset'] = elem1.text
        if elem1.tag == 'trunkExcel' and elem1.text is not None:
            configs['trunkExcel'] = elem1.text

        if elem1.tag == 'currentServer':
            for elem2 in elem1.iter():
                if elem2.tag != 'currentServer' and elem2.text is not None:
                    currentServerList.append(elem2.text)
        configs['currentServer'] = currentServerList
        if elem1.tag == 'currentAsset' and elem1.text is not None:
            configs['currentAsset'] = elem1.text
        if elem1.tag == 'currentExcel' and elem1.text is not None:
            configs['currentExcel'] = elem1.text

        if elem1.tag == 'nextServer':
            for elem2 in elem1.iter():
                if elem2.tag != 'nextServer' and elem2.text is not None:
                    nextServerList.append(elem2.text)
        configs['nextServer'] = nextServerList
        if elem1.tag == 'nextAsset' and elem1.text is not None:
            configs['nextAsset'] = elem1.text
        if elem1.tag == 'nextExcel' and elem1.text is not None:
            configs['nextExcel'] = elem1.text

    return configs
