"""
add_sel_to_displayer.py
"""
import maya.cmds as cmds

my_sel = cmds.ls(sl=True)
layer_sel = cmds.ls(type='displayLayer')
for i in layer_sel:
    print i
cmds.editDisplayLayerMembers('displayLayer1', my_sel)
