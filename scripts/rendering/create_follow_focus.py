#!/usr/bin/env python
"""
create_follow_focus.py
Description of create_follow_focus.py.
"""

import maya.cmds as cmds

sel_nodes = cmds.ls(sl=True)

if sel_nodes:
    cmds.distanceDimension(sp=(0, 0, 1), ep=(0, 0, 0))
    rename_locator1 = cmds.rename("locator1", sel_nodes[0]+"FfCam_LOC")
    rename_locator2 = cmds.rename("locator2", sel_nodes[0]+"FfFocalPt_LOC")
    rename_distance = cmds.rename("distanceDimension1", sel_nodes[0]+"FfDistance_DIST")


    # Set color of the focus plane locator
    cmds.setAttr(rename_locator2+".overrideEnabled", 1)
    cmds.setAttr(rename_locator2+".overrideColor", 18)

    cmds.parentConstraint(sel_nodes[0], rename_locator1, maintainOffset=False)
    cmds.aimConstraint(sel_nodes[0], rename_locator2, maintainOffset=False)

    # Lock and hide translation and rotation for cam locator
    cmds.setAttr(rename_locator1+'.tx', lock=True, keyable=False, channelBox=False)
    cmds.setAttr(rename_locator1+'.ty', lock=True, keyable=False, channelBox=False)
    cmds.setAttr(rename_locator1+'.tz', lock=True, keyable=False, channelBox=False)
    cmds.setAttr(rename_locator1+'.rx', lock=True, keyable=False, channelBox=False)
    cmds.setAttr(rename_locator1+'.ry', lock=True, keyable=False, channelBox=False)
    cmds.setAttr(rename_locator1+'.rz', lock=True, keyable=False, channelBox=False)

    cmds.group(rename_locator1, rename_locator2, rename_distance, n=sel_nodes[0]+"FollowFocus_GRP")
else:
    cmds.warning("Nothing is selected")
