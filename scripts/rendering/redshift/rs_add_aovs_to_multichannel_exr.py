#!/usr/bin/env python
"""
rs_add_aovs_to_multichannel_exr.py

Set the file name prefix of redshift AOVs.
"""
import maya.cmds as cmds

def addAovsToExr():
    all_nodes = cmds.ls()
    node_filter = "rsAov_"

    all_nodes = cmds.ls()
    for node in all_nodes:
        if node.startswith(node_filter):
            cmds.setAttr(node+".filePrefix", "<BeautyPath>/<BeautyFile>", type='string')
            print node+" has been added to multichannel exr."

    cmds.warning("AOVs have been added to multichannel exr.")