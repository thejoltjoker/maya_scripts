#!/usr/bin/env python3
"""create_turnaround_camera.py
Description of create_turnaround_camera.py.
"""
from maya import cmds


def get_active_camera():
    camera = 'persp'
    for vp in cmds.getPanel(type="modelPanel"):
        camera = cmds.modelEditor(vp, q=1, av=1, cam=1)
    return camera


def main():
    """docstring for main"""
    print('HEJ')
    camera = get_active_camera()

if __name__ == '__main__':
    main()
