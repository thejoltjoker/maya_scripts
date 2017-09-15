#!/usr/bin/env python
"""
cam_loc_scale.py
Description of Description of cam_loc_sca.py.
"""
import maya.cmds as cmds


def main():
    """docstring for function"""
    sel = cmds.ls(selection=True)

    for i in sel:
        cam = cmds.listRelatives(shapes=True)

        for c in cam:
            curVal = cmds.getAttr(c + '.locatorScale')
            newVal = curVal * 1.25
            print newVal
            cmds.setAttr(c + '.locatorScale', newVal)


if __name__ == '__main__':
    main()
