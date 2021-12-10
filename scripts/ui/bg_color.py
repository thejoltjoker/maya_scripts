#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bg_color.py

Change viewport background color
"""

import maya.cmds as cmds
import os


def hex_to_rgb(hex):
    """Get RGB value from hex

    Args:
        hex: string

    Returns:
        tuple(r, g, b)
    """
    h = hex.strip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def change_bg_color(hex):
    """Change the viewport background color"""
    color = hex_to_rgb(hex)
    cmds.displayRGBColor('background', *color)


if __name__ == '__main__':
    result = cmds.promptDialog(
        title='Change BG color',
        message='Enter hex value:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'OK':
        hex = cmds.promptDialog(query=True, text=True)
        change_bg_color(hex)

# Change viewport background color
# //
# int $toggled_color
# if($toggled_color == 0)
# {
#     displayRGBColor "background" 1. 1. 1.
#     $toggled_color = 1
# }
# else
# {
#     displayRGBColor "background" 0.688 0.688 0.688
#     $toggled_color = 0
# }
# //
