#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
maya_scripts_folder_to_menu.py
Description of maya_scripts_folder_to_menu.py.
"""

import maya.cmds as cmds
import os
from pprint import pprint
import logging

SCRIPTS_PATH = r'C:\Users\JohannesAndersson\OneDrive - Frank Valiant AB\Desktop\scripts\maya_scripts\scripts'


def get_icon(path):
    """Get the icon for the given file or directory"""
    if os.path.isdir(path):
        icon = os.path.join(path, os.path.basename(path) + '.png')
    else:
        icon = os.path.splitext(path)[0] + '.png'

    if not os.path.isfile(icon):
        icon = ''

    return icon


def create_submenu(parent, structure):
    """Create a submenu"""
    for k in sorted(structure, key=structure.get, reverse=True):
        v = structure.get(k)
        print k + ': ' + str(v)
        icon = get_icon(k)

        if v:
            menu_item = cmds.menuItem(subMenu=True,
                                      parent=parent,
                                      label=parse_filename(k),
                                      fi=icon,
                                      i=icon,
                                      tearOff=True)
            # Create title for sub menu
            cmds.menuItem(parent=menu_item,
                          label=parse_filename(k),
                          fi=icon,
                          i=icon,
                          enable=False)
            cmds.menuItem(divider=True)

            create_submenu(menu_item, v)
        else:
            if k.endswith('.py'):
                with open(k, 'r') as p:
                    pscript = p.readlines()
                menu_item = cmds.menuItem(parent=parent,
                                          label=parse_filename(k),
                                          # i=icon,
                                          command='\n'.join(pscript))
    return


def create_menu():
    structure = path_to_dict(SCRIPTS_PATH)
    pprint(structure)
    menu_id = 'custom_scripts_menu'
    # enhancify_maya_path = os.path.dirname(os.path.realpath(__file__))
    # maya_menu_path = os.path.dirname(os.path.realpath(__file__))

    # Delete menu if it already exists
    if cmds.menu(menu_id, exists=True):
        cmds.deleteUI(menu_id)

    # Create menu
    menu_obj = cmds.menu(menu_id,
                         allowOptionBoxes=True,
                         parent='MayaWindow',
                         label='Custom Scripts',
                         tearOff=True)
    cmds.menuItem(parent=menu_id,
                  label='Reload',
                  enable=False)
    cmds.menuItem(divider=True)

    create_submenu(menu_id, structure)


def parse_filename(filename):
    """Generates a readable name from snake case filename"""
    basename = os.path.basename(filename)
    return os.path.splitext(basename)[0].replace("_", " ").title()


def path_to_dict(path):
    d = {}
    paths = [os.path.join(path, x) for x in sorted(os.listdir(path)) if x != '__init__.py']
    paths = [x for x in paths if os.path.isdir(x) or x.endswith('.py')]

    # Remove dotfiles
    paths = [x for x in paths if not os.path.basename(x).startswith('.')]

    for f in sorted(paths):
        if os.path.isdir(os.path.join(path, f)):
            d[f] = path_to_dict(os.path.join(path, f))
        else:
            d[f] = {}
    return d


if __name__ == '__main__':
    pprint(path_to_dict(SCRIPTS_PATH))
    create_menu()
