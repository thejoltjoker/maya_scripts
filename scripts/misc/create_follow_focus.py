#!/usr/bin/env python
"""
create_follow_focus.py
Description of create_follow_focus.py.
"""

import maya.cmds as cmds

def create_follow_focus():
    sel_nodes = cmds.ls(sl=True)

    if sel_nodes:
        cam_shape = cmds.listRelatives(shapes=True)

        distance_node = cmds.distanceDimension(sp=(0, 0, 1), ep=(0, 0, 0))
        distance_node_locators = cmds.listConnections(distance_node)
        rename_locator1 = cmds.rename(distance_node_locators[0], sel_nodes[0]+"FfCam_LOC")
        rename_locator2 = cmds.rename(distance_node_locators[1], sel_nodes[0]+"FfFocalPt_LOC")
        rename_distance = cmds.rename("distanceDimension1", sel_nodes[0]+"FfDistance_DIST")
        print rename_distance

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

        for shape in cam_shape:
            cmds.connectAttr(rename_distance+'.distance', shape+'.focusDistance')

    else:
        cmds.warning("Nothing is selected")
create_follow_focus()