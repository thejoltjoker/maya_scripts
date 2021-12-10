#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    vertPosX = []
    vertPosY = []
    vertPosZ = []

    selection = cmds.ls(sl=True)
    centerObj = selection[-1]
    del selection[-1]

    for i in selection:
        cmds.select(i)
        vertPos = cmds.xform(q=True, ws=True, t=True)

        # x pos
        vertPosX.extend(vertPos[0::3])
        # y pos
        vertPosY.extend(vertPos[1::3])
        # z pos
        vertPosZ.extend(vertPos[2::3])

    xAverage = reduce(lambda x, y: x + y, vertPosX) / len(vertPosX)
    yAverage = reduce(lambda x, y: x + y, vertPosY) / len(vertPosY)
    zAverage = reduce(lambda x, y: x + y, vertPosZ) / len(vertPosZ)

    print xAverage
    print yAverage
    print zAverage
    cmds.setAttr(centerObj + '.translateX', xAverage)
    cmds.setAttr(centerObj + '.translateY', yAverage)
    cmds.setAttr(centerObj + '.translateZ', zAverage)

    cmds.select(centerObj)
    print "END"


if __name__ == '__main__':
    main()
