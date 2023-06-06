#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""

import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.cmds as cmds


def get_or_create_layer(name):
    rs = renderSetup.instance()
    # Create and append the render layer
    try:
        rl = rs.getRenderLayer(name)
    except Exception as e:
        rl = rs.createRenderLayer(name)
    return rl


def create_layer(layer_name, nodes=None, collections=None):
    # Get selected objects
    camera = cmds.ls(selection=True)[0]
    layerName = camera.split(':')[1].replace('_cam', '')
    camShape = cmds.listRelatives(camera, shapes=True)[0]

    # Get frame range
    frames = cmds.getAttr(camShape + '.notes').split('-')
    startFrame = frames[0].rstrip()
    endFrame = frames[-1].rstrip()

    camCol = rl.createCollection('cam_' + layerName)
    camSel = camCol.getSelector()
    camSel.setPattern(camera)
    camSSel = camSel.staticSelection
    camSSel.add(camera)
    camSSel.add(camShape)
    camCol.createAbsoluteOverride(cam, 'renderable')

    cmds.setAttr(cam + '.renderable', 1)

    # Create and append 2 collections
    include = rl.createCollection("include")
    include.getSelector().setPattern('*')

    # Create exclude collection
    exclude = rl.createCollection("exclude")
    exclude.setSelfEnabled(False)

    # Switch to new layer
    rs.switchToLayer(rl)

    # Frame range
    rsInstance = rl.renderSettingsCollectionInstance()
    rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'startFrame')
    rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'endFrame')
    cmds.setAttr('defaultRenderGlobals.startFrame', startFrame)
    cmds.setAttr('defaultRenderGlobals.endFrame', endFrame)

    current_layer = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
    for cam in cmds.ls(cameras=True):
        cmds.editRenderLayerAdjustment(cam + '.primaryEngine')
        cmds.setAttr(cam + '.primaryEngine', 0)


def main():
    """docstring for main"""
    pass


if __name__ == '__main__':
    main()
