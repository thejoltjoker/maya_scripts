#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
scripts_to_menu.py
Description of scripts_to_menu.py.
"""

import maya.cmds as cmds
import os
import re
from pprint import pprint
import logging

SCRIPTS_PATH = r'C:\Users\JohannesAndersson\OneDrive - Frank Valiant AB\Desktop\scripts\maya_scripts\scripts'
ICONS_PATH = os.path.join(SCRIPTS_PATH, '.icons')


#
# from importlib import reload  # Python 3.4+
#
# rn = reload(rn)


def reload(*args, **kwargs):
    create_menu()


def get_icon(path):
    """Get the icon for the given file or directory"""

    # If folder, use the image inside with the same name
    if os.path.isdir(path):
        icon = os.path.join(ICONS_PATH, os.path.basename(path) + '.png')
    else:
        # If file just use image with same name in same folder
        icon = os.path.join(ICONS_PATH, os.path.splitext(os.path.basename(path))[0] + '.png')

    # If image doesn't exist, use nothing
    if not os.path.isfile(icon):
        icon = ''

    return icon


def get_docstring(file):
    logging.debug(file)
    with open(file, "r") as f:
        content = f.read()  # read file
        pattern = re.compile(r'"""([\s\S]*?)"""')  # create docstring pattern
    found = re.findall(pattern, content)
    if found:
        return found[0].strip().replace('\n', '- ')


def create_submenu(parent, structure):
    """Create a submenu"""
    for k in sorted(structure):
        parsed_name = parse_filename(k)

        # Get annotation from docstring
        annotation = parsed_name
        if os.path.isfile(k):
            annotation = get_docstring(k)

        v = structure.get(k)
        logging.debug(k + ': ' + str(v))
        # print k + ': ' + str(v)
        icon = get_icon(k)

        if v:
            menu_item = cmds.menuItem(subMenu=True,
                                      parent=parent,
                                      label=parsed_name,
                                      fi=icon,
                                      i=icon,
                                      tearOff=True)
            # Create title for sub menu
            cmds.menuItem(parent=menu_item,
                          label=parsed_name,
                          fi=icon,
                          i=icon,
                          enable=False)
            cmds.menuItem(divider=True)

            create_submenu(menu_item, v)
        else:
            if k.endswith('.py'):
                # print k
                with open(k, 'r') as p:
                    pscript = p.readlines()
                menu_item = cmds.menuItem(parent=parent,
                                          label=parsed_name,
                                          i=icon,
                                          annotation=annotation,
                                          command='\n'.join(pscript))
    return


def create_menu():
    structure = path_to_dict(SCRIPTS_PATH)
    # pprint(structure)
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
                         label='Script Kiddie',
                         tearOff=True)
    cmds.menuItem(parent=menu_id,
                  label='Reload',
                  i=os.path.join(ICONS_PATH, 'reload.png'),
                  enable=True,
                  c=reload)
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
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # pprint(path_to_dict(SCRIPTS_PATH))
    create_menu()
