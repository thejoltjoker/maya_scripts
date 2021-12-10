#!/usr/bin/env python
"""
Export obj for mari
"""
import sys
import os
import time
import re
import maya.cmds as cmds

cur_script_path = os.path.dirname(os.path.realpath(__file__))

# Developer path fix
local_script_path = r'D:\people\johannes\scripts\repos'
if local_script_path in cur_script_path:
    cur_script_path = cur_script_path.replace(local_script_path, r'P:\_Scripts\Python')

exports_folder_name = 'exports'
exports_folder_path = os.path.join(cur_script_path, exports_folder_name)

# Make a new filename based on current filename
cur_file_name = cmds.file(q=True, sn=True)
print "var cur_file_name = "+cur_file_name
# cur_file_name_short = cmds.file(q=True, sn=True, shn=True)
split_cur_file_name = cur_file_name.rsplit('_', 1)
add_to_name = "toMari"
split_cur_file_name.insert(-1, add_to_name)

split_cur_file_name_noext = os.path.splitext(split_cur_file_name)[0]

sep = "_"


render_file_name = sep.join(split_cur_file_name_noext)

def export():
    """Export selected object(s)"""

    file_ext = '.obj'

    # Get selection
    sel = cmds.ls(sl=True)

    if sel:
        filename = '_'.join([cur_date, obj_name_alpha])+file_ext

        thumb_filename = '_'.join([cur_date, obj_name_alpha, 'thumb'])+'.png'

        export_file = os.path.join(export_folder_path, filename)
        export_file_thumb = os.path.join(exports_folder_path, thumb_filename)
        print export_file

        cmds.file(export_file, type=file_type, es=True)

        if len(sel) > 1:
            cmds.warning('Objects copied to '+export_file)
        else:
            cmds.warning(obj_name+' copied to '+export_file)

    else:
        cmds.warning('Nothing is selected.')

def thumbnail():
    cur_frame = cmds.currentTime( query=True )
    model_panel = cmds.paneLayout('viewPanes', q=True, pane1=True)
    print model_panel
    cmds.isolateSelect(model_panel, state=1)
    cmds.playblast(fr=cur_frame, fmt='image', compression='png', cf=export_file_thumb, orn=False, v=False)
    cmds.isolateSelect(model_panel, state=0)