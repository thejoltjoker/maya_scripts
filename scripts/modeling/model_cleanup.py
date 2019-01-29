#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
model_cleanup.py
Description of model_cleanup.py.
"""
import maya.cmds as cmds
import maya.mel as mel


def delete_sets():
    objectSetsList = cmds.ls('set*', type='objectSet')
    for i in objectSetsList:
        if cmds.objectType(i, isType='objectSet'):
            cmds.delete(i)


def delete_disp_layers():
    disp_layers = [x for x in cmds.ls() if cmds.nodeType(x) == 'displayLayer']
    disp_layers.remove('defaultLayer')
    for n in disp_layers:
        cmds.delete(n)


def delete_all_history():
    mel.eval('DeleteAllHistory')


def main():
    """run all functions"""
    delete_sets()
    delete_disp_layers()
    delete_all_history()


if __name__ == '__main__':
    main()
