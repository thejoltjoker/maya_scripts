#!/usr/bin/env python3
"""toggle_dof_on_camera.py
Description of toggle_dof_on_camera.py.
"""
from maya import cmds


def main():
    """docstring for main"""
    cameras = cmds.ls(sl=True)
    if cameras:
        for cam in cameras:
            dof = cmds.getAttr(cam + ".depthOfField")
            if dof:
                cmds.setAttr(cam + ".depthOfField", 0)
                cmds.warning('Depth of field was disabled')
            else:
                cmds.setAttr(cam + ".depthOfField", 1)
                cmds.warning('Depth of field was enabled')


if __name__ == '__main__':
    main()
