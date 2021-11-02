#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds
import os
import shutil


def list_textures():
    """List all textures in scene"""

    # Gets all 'file' nodes in maya
    return [cmds.getAttr(x + '.fileTextureName') for x in cmds.ls(type='file')]


def copy_files(destination_path=None):
    """docstring for main"""
    failed = []
    # Default to desktop
    if destination_path is None:
        path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    else:
        path = destination_path
    textures = list_textures()
    print 'Copying ' + str(len(textures)) + ' files'
    for n, f in enumerate(textures, 1):
        try:
            print str(n) + '/' + str(len(textures))
            shutil.copy2(f, os.path.join(path, os.path.basename(f)))
            print 'Successfully copied ' + os.path.basename(f) + ' to ' + os.path.join(path, os.path.basename(f))
        except:
            failed.append(f)

    if failed:
        print 'Failed to copy the following textures:'
        for i in failed:
            print i
    # print destination_path


if __name__ == '__main__':
    result = cmds.promptDialog(
        title='Collect textures',
        message='Where do you want to put the textures? (will overwrite existing!)',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'OK':
        path = cmds.promptDialog(query=True, text=True)
        copy_files(path)
