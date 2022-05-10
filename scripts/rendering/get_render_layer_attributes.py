#!/usr/bin/env python3
"""get_render_layer_attributes.py
Description of get_render_layer_attributes.py.
"""
from pprint import pprint

import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
from maya import cmds


def get_callable_attributes(obj):
    """Returns the callable attributes of an object"""

    callable_attrs = {}
    for attr in dir(obj):
        attr_obj = getattr(obj, attr)
        if callable(attr_obj):
            callable_attrs[attr] = attr_obj
    return callable_attrs


def render_layers():
    return cmds.ls(type='renderLayer')


def is_render_layer_enabled(render_layer: renderLayer):
    return render_layer.isEnabled()


def render_layer_frame_range(render_layer: renderLayer, multiplier=240):
    """Get frame range from a render layer if it's overridden"""
    # Current frame range as default values
    start_frame = cmds.getAttr('defaultRenderGlobals.startFrame')
    end_frame = cmds.getAttr('defaultRenderGlobals.endFrame')

    # Iterate over collections and overrides to get the right attributes
    collections = render_layer.getCollections()
    if collections:
        for collection in collections:
            overrides = collection.getOverrides()
            if overrides:
                for override in overrides:
                    if override.name() == 'startFrame':
                        start_frame = override.getAttrValue() / multiplier
                    elif override.name() == 'endFrame':
                        end_frame = override.getAttrValue() / multiplier

    return start_frame, end_frame


def main():
    """docstring for main"""
    for i in cmds.renderSetup(q=True, renderLayers=True):
        print(i)
    render_setup = renderSetup.instance()
    render_layers = render_setup.getRenderLayers()

    for render_layer in render_layers:
        render_layer_name = render_layer.name()  # Without "rs_" prefix
        print(render_layer_name)
        print(render_layer_frame_range(render_layer))
    # attrs = get_callable_attributes(collections[0])
    # for i in attrs:
    #     print(i)
    # callable_attrs = get_callable_attributes(render_layer)
    # for callable_function in callable_attrs:
    #     print(callable_function)


if __name__ == '__main__':
    main()
