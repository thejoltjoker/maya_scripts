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
    rl = get_or_create_layer(layer_name)
    # Get selected objects
    # camera = cmds.ls(selection=True)[0]
    # layerName = camera.split(':')[1].replace('_cam', '')
    # camShape = cmds.listRelatives(camera, shapes=True)[0]

    # Set render settings
    # Override frame range
    rsInstance = rl.renderSettingsCollectionInstance()
    rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'startFrame')
    rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'endFrame')
    # Enable AOVs
    redshift_options = cmds.ls('redshiftOptions', an=True)
    if redshift_options:
        redshift_options = redshift_options[0]
        cmds.setAttr(f'{redshift_options}.aovGlobalEnableMode', 1)

    # Create BASE_GRP
    base_group = rl.createGroup(f'{layer_name}_BASE_GRP')
    # Create FOREGROUND
    foreground_col = base_group.createCollection(f'{layer_name}_FOREGROUND_COL')
    foreground_col.setSelectorType('sets')
    foreground_col_filter =
    fg_transform_col = foreground_col.createCollection(f'{layer_name}_FG_TRANSFORM_COL')
    fg_shape_col = fg_transform_col.createCollection(f'{layer_name}_FG_SHAPE_COL')
    fg_shape_col.createAbsoluteOverride('primaryVisibility', 1)

    # camCol = rl.createCollection('cam_' + layerName)
    # camSel = camCol.getSelector()
    # camSel.setPattern(camera)
    # camSSel = camSel.staticSelection
    # camSSel.add(camera)
    # camSSel.add(camShape)
    # camCol.createAbsoluteOverride(cam, 'renderable')
    #
    # cmds.setAttr(cam + '.renderable', 1)
    #
    # # Create and append 2 collections
    # include = rl.createCollection("include")
    # include.getSelector().setPattern('*')
    #
    # # Create exclude collection
    # exclude = rl.createCollection("exclude")
    # exclude.setSelfEnabled(False)

    # Switch to new layer
    rs.switchToLayer(rl)

    current_layer = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
    # for cam in cmds.ls(cameras=True):
    #     cmds.editRenderLayerAdjustment(cam + '.primaryEngine')
    #     cmds.setAttr(cam + '.primaryEngine', 0)


def main():
    """docstring for main"""
    create_layer('s010')


if __name__ == '__main__':
    main()
