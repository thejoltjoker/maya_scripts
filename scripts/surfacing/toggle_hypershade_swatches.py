#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.

Credit: https://lesterbanks.com/2013/10/disabling-color-swatches-in-maya/
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    swatch_state = cmds.renderThumbnailUpdate(q=True)
    if swatch_state == 0:
        cmds.renderThumbnailUpdate(1)
        print('Swatches turned ON')
    else:
        cmds.renderThumbnailUpdate(0)
        print('Swatches turned OFF')

if __name__ == '__main__':
    main()
