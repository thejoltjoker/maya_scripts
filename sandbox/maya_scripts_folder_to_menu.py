#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
maya_scripts_folder_to_menu.py
Description of maya_scripts_folder_to_menu.py.
"""

import maya.cmds as cmds
import os


def menu():
    # TEST
    cmds.menuItem(divider=True)

    # Experimental tools
    cmds.menuItem(subMenu=True,
                  label='Scripts',
                  parent=self.menu,
                  i=os.path.join(menu_icons_path, 'alpha.png'),
                  tearOff=True)

    # for s
    # # Sanity check - Needs to rework ui
    # cmds.menuItem(label='Sanity check',
    #               i=os.path.join(menu_icons_path, 'eye.png'),
    #               c=self.tool_render_sanity_check)


def main():
    """docstring for main"""
    maya_scripts_folder = r"E:\Dropbox\scripts\repos\maya\scripts"
    for root, dirs, files in os.walk(maya_scripts_folder):
        # for name in files:
        #     print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

    subfolders = [x for x in os.listdir(maya_scripts_folder) if os.path.isdir(
        os.path.join(maya_scripts_folder, x))]
    for i in os.listdir(maya_scripts_folder):
        print os.path.isdir(i)


if __name__ == '__main__':
    main()
