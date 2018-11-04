#!/usr/bin/env python
"""
toggle_motion_blur.py
Description of toggle_motion_blur.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    font_color = '#0cf'
    if cmds.getAttr('redshiftOptions.motionBlurEnable'):
        cmds.setAttr('redshiftOptions.motionBlurEnable', 0)
        cmds.inViewMessage(
            smg='<font color={}>Motion blur:</font> Disabled'.format(
                font_color),
            bkc=0x00262626,
            pos='topRight',
            fade=True,
            a=0.5)
    else:
        cmds.setAttr('redshiftOptions.motionBlurEnable', 1)
        cmds.inViewMessage(
            smg='<font color={}>Motion blur:</font> Enabled'.format(
                font_color),
            bkc=0x00262626,
            pos='topRight',
            fade=True,
            a=0.5)


if __name__ == '__main__':
    main()
