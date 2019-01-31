#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    building001 = [x for x in cmds.ls(
        type='transform') if 'buildingLow001' in x]
    building002 = [x for x in cmds.ls(
        type='transform') if 'buildingLow002' in x]
    building003 = [x for x in cmds.ls(
        type='transform') if 'buildingLow003' in x]
    destBuilding002 = [x for x in cmds.ls(
        type='transform') if 'destroyedBuilding02Low' in x]
    cmds.sets(building001, e=True,
              forceElement='sthlm:simplifiedBuildings:lambert4SG')
    cmds.sets(building002, e=True,
              forceElement='sthlm:simplifiedBuildings:lambert5SG')
    cmds.sets(building003, e=True,
              forceElement='sthlm:simplifiedBuildings:lambert6SG')
    cmds.sets(destBuilding002, e=True,
              forceElement='sthlm:destroyedBuilding02:lambert2SG')


if __name__ == '__main__':
    main()
