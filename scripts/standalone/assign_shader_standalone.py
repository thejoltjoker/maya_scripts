#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
incremental_save.py
Description of incremental_save.py.
"""
import maya.standalone
import maya.cmds as cmds
import os
import re


def main():
    maya.standalone.initialize()
    cmds.file(r'path/to/maya/file.ma', open=True)

    shading_group = 'material_shadingGroup'

    cmds.sets(['mesh01_GEO',
               'mesh02_GEO',
               'mesh03_GEO'],
              e=True,
              forceElement=shading_group)

    # Save file
    cmds.file(save=True)
    maya.standalone.uninitialize()


if __name__ == '__main__':
    main()
