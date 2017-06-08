#!/usr/bin/env python
"""
open_scene_folder.py

Open the folder of the currently open scene.
"""
import os
import maya.cmds as cmds
cur_file = cmds.file(q=True, sn=True)
cur_file_folder = os.path.dirname(cur_file)
os.startfile(cur_file_folder)