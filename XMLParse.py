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

        if elem1.tag == 'trunkServer':
            for elem2 in elem1.iter():
                if elem2.tag != 'trunkServer':
                    trunkServerList.append(elem2.text)
        configs['trunkServer'] = trunkServerList
        if elem1.tag == 'trunkAsset':
            configs['trunkAsset'] = elem1.text
        if elem1.tag == 'trunkExcel':
            configs['trunkExcel'] = elem1.text

        if elem1.tag == 'currentServer':
            for elem2 in elem1.iter():
                if elem2.tag != 'currentServer':
                    currentServerList.append(elem2.text)
        configs['currentServer'] = currentServerList
        if elem1.tag == 'currentAsset':
            configs['currentAsset'] = elem1.text
        if elem1.tag == 'currentExcel':
            configs['currentExcel'] = elem1.text

        if elem1.tag == 'nextServer':
            for elem2 in elem1.iter():
                if elem2.tag != 'nextServer':
                    nextServerList.append(elem2.text)
        configs['nextServer'] = nextServerList
        if elem1.tag == 'nextAsset':
            configs['nextAsset'] = elem1.text
        if elem1.tag == 'nextExcel':
            configs['nextExcel'] = elem1.text

    return configs
