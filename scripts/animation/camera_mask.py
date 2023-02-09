#!/usr/bin/env python3
"""camera_mask.py
Description of camera_mask.py.
"""
from maya import cmds


def active_camera():
    panel = cmds.getPanel(withFocus=True)
    cam_shape = cmds.modelEditor(panel, q=1, av=1, cam=1)

    if cmds.listRelatives(cam_shape, p=True):
        return cmds.listRelatives(cam_shape, p=True)[0]
    return None


def main():
    """docstring for main"""
    # camera -e -filmFit horizontal s020_cam;
    camera = active_camera()
    if camera:
        cmds.camera(camera, e=True, filmFit='horizontal')


if __name__ == '__main__':
    main()
