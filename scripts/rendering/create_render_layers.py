#!/usr/bin/env python3
"""
create_render_layers.py
Create render layers using the "new" render setup in Maya (since 2017)
"""
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger()
from pprint import pprint

import maya.app.renderSetup.model.override as renderOverride
import maya.app.renderSetup.model.selector as renderSelector
import maya.app.renderSetup.model.collection as renderCollection
import maya.app.renderSetup.model.group as renderGroup
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.cmds as cmds


def render_setup_instance():
    """Create a render setup instance

    Returns:
        maya.app.renderSetup.model.renderSetup.RenderSetup()
    """
    return renderSetup.instance()


def get_or_create_layer(render_setup, name):
    """Get an existing or create a new render layer

    Args:
        name (str): the name of the layer
        render_setup (renderSetup.RenderSetup):
    """
    try:
        layer = render_setup.getRenderLayer(name)
    except Exception as e:
        layer = render_setup.createRenderLayer(name)
    return layer


def override_frame_range(layer, start_frame, end_frame, multiplier=240):
    """Create a render settings override for the frame range, on the given layer

    Args:
        layer (maya.app.renderSetup.model.renderLayer.RenderLayer): the render layer
        start_frame: start frame
        end_frame: end frame
        multiplier: multiplier to fix maya frame range wonkiness
    """
    set_render_settings_override(layer, 'startFrame', start_frame * multiplier)
    set_render_settings_override(layer, 'endFrame', end_frame * multiplier)


def set_render_settings_override(layer, attribute, value):
    """Set an override for the render settings

    Args:
        layer (maya.app.renderSetup.model.renderLayer.RenderLayer): the render layer
        attribute: the attribute in defaultRenderGlobals to override
        value: value

    Returns:
        maya.app.renderSetup.model.collection.Collection: the override collection
        
    """
    # Create override
    overridden = False
    collection = layer.renderSettingsCollectionInstance()
    overrides = collection.getOverrides()
    if overrides:
        for override in overrides:
            if override.name() == attribute:
                override.setAttrValue(value)
                overridden = True
    if not overridden:
        override = collection.createAbsoluteOverride('defaultRenderGlobals', attribute)
        override.setAttrValue(value)
        overridden = True

    return collection


# def create_layer(layer_name, nodes=None, collections=None):
#     camCol = rl.createCollection('cam_' + layerName)
#     camSel = camCol.getSelector()
#     camSel.setPattern(camera)
#     camSSel = camSel.staticSelection
#     camSSel.add(camera)
#     camSSel.add(camShape)
#     camCol.createAbsoluteOverride(cam, 'renderable')
#
#     cmds.setAttr(cam + '.renderable', 1)
#
#     # Create and append 2 collections
#     include = rl.createCollection("include")
#     include.getSelector().setPattern('*')
#
#     # Create exclude collection
#     exclude = rl.createCollection("exclude")
#     exclude.setSelfEnabled(False)
#
#     # Switch to new layer
#     rs.switchToLayer(rl)
#
#     # Frame range
#     rsInstance = rl.renderSettingsCollectionInstance()
#     rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'startFrame')
#     rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'endFrame')
#     cmds.setAttr('defaultRenderGlobals.startFrame', startFrame)
#     cmds.setAttr('defaultRenderGlobals.endFrame', endFrame)
#
#     current_layer = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
#     for cam in cmds.ls(cameras=True):
#         cmds.editRenderLayerAdjustment(cam + '.primaryEngine')
#         cmds.setAttr(cam + '.primaryEngine', 0)


def get_or_create_collection(parent, name, suffix='col'):
    """Get an existing or create a new collection

    Args:
        parent: layer, collection or group
        name: name of the collection

    Returns:
        maya.app.renderSetup.model.collection.Collection: the collection
    """
    name = f'{name}_{suffix}' if suffix else name
    collection = None
    # if isinstance(parent, renderLayer.RenderLayer):
    #     children = parent.getChildren()
    try:
        children = parent.getChildren(renderCollection.Collection)
    except:
        children = parent.getCollections()

    for child in children:
        if child.name() == name:
            collection = child
    if not collection:
        collection = parent.createCollection(name)

    return collection


def get_or_create_set(name, children=None):
    """Get an existing or create a new set

    Args:
        name: the name of the set
        children: the nodes to put in the set

    Returns:
        str: set name
    """
    if cmds.ls(name):
        if cmds.nodeType(name) != 'objectSet':
            node = cmds.sets(n=name, em=True)
        else:
            node = cmds.ls(name)[0]
    else:
        node = cmds.sets(n=name, em=True)

    if children:
        cmds.sets(children, include=node)

    return node


def create_sets(name, nodes=None, parent=None):
    """Create a list of sets

    Args:
        name:
        nodes:
        parent:

    Returns:

    """
    cmds.select(clear=True)

    foreground = get_or_create_set(f'{name}_foreground')
    background = get_or_create_set(f'{name}_background')
    exclude = get_or_create_set(f'{name}_exclude')
    container = get_or_create_set(name, [foreground, background, exclude])
    return container


def get_or_create_group(parent, name):
    """Get an existing or create a new group

    Args:
        parent: layer, collection or group
        name: name of the group

    Returns:
        maya.app.renderSetup.model.group.Group: the group
    """
    group = None
    children = parent.getGroups()
    for child in children:
        if child.name() == name:
            group = child
    if not group:
        group = parent.createGroup(name)
    return group


def set_collection_filters(collection, pattern='', filter_type=0, custom_filter_type=''):
    """Set filter parameters for a collection

    Args:
        collection (maya.app.renderSetup.model.collection.Collection): the collection
        pattern (str): naming pattern
        filter_type (int): the index of the filter type
        custom_filter_type (str): the custom filter

    Returns:
        maya.app.renderSetup.model.collection.Collection
    """
    selector = collection.getSelector()

    if filter_type == 8:
        selector.setFilterType(filter_type)
        selector.setCustomFilterValue(custom_filter_type)
    else:
        selector.setFilterType(filter_type)

    selector.setPattern(pattern)

    return collection


def add_static_selection(collection, nodes: list):
    """Add specific nodes to collection

    Args:
        collection:
        nodes:

    Returns:

    """
    selector = collection.getSelector()
    static_selector = selector.staticSelection
    static_selector.add(nodes)
    return collection


def set_override(collection, node, attribute, value):
    """Set an override in the given collection

    Args:
        collection:
        node:
        attribute:
        value:

    Returns:

    """
    # Create override
    override = None
    overridden = False

    # Check for existing overrides and change value
    overrides = collection.getOverrides()
    if overrides:
        for override in overrides:
            if override.name() == attribute:
                override.setAttrValue(value)
                overridden = True

    # Create new override and set value
    if not overridden:
        override = collection.createAbsoluteOverride(node, attribute)
        override.setAttrValue(value)
        overridden = True

    return override


def main():
    """docstring for main"""
    name = 'test'
    layer_name = f'{name}_main'

    # Create sets
    create_sets(name)

    # Create render setup instance
    rs = render_setup_instance()

    # Get or create a layer
    layer = get_or_create_layer(rs, layer_name)

    # Set render settings overrides
    start_frame = random.randint(1, 10)
    end_frame = random.randint(11, 100)
    override_frame_range(layer, start_frame, end_frame)

    # Create group
    group = get_or_create_group(layer, layer_name + '_base_grp')

    # Create collections
    # foreground_col = get_or_create_collection(group, layer_name + '_fg_col')
    # set_collection_filters(foreground_col, filter_type=5, pattern=layer_name + '_set')
    # foreground_transform_col = get_or_create_collection(foreground_col, layer_name + '_fg_transform')
    # set_collection_filters(foreground_transform_col, filter_type=1)
    # foreground_shape_col = get_or_create_collection(foreground_transform_col, layer_name + '_fg_shape')
    # set_collection_filters(foreground_shape_col, filter_type=2)

    # Camera collection
    camera = cmds.camera()
    camera_shape = camera[1]
    camera_col = get_or_create_collection(group, layer_name + '_cam_col')
    set_collection_filters(camera_col, filter_type=8, pattern=camera_shape, custom_filter_type='camera')
    set_override(camera_col, camera_shape, 'renderable', True)
    # render.instance().decode(json.load(tempRead), render.DECODE_AND_RENAME, None)


if __name__ == '__main__':
    main()
