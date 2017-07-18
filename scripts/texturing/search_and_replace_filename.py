#!/usr/bin/env python
"""
search_and_replace_filename.py
Description of search_and_replace_filename.py.
"""

import maya.cmds as cmds

sel_nodes = cmds.ls(sl=True)

search_for = '\Volumes\live_projects'
replace_with = r'\\SEQ-LIVE\live_projects'

for node in sel_nodes:
    if cmds.nodeType(node) == 'file':
        texture_path = cmds.getAttr(node+".fileTextureName")
        new_texture_path = texture_path.replace(search_for, replace_with)
        cmds.setAttr(node+".fileTextureName", new_texture_path, type='string')

        print "Path changed from "+texture_path+" to "+new_texture_path+" on node "+node
