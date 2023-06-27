#!/usr/bin/env python3
"""maya_render_setup.py
Various functions for working with maya render setup.
"""
from maya import cmds, mel
import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.app.renderSetup.model.connectionOverride as connectionOverride


def currently_enabled_layer_name():
    # Get the currently enabled render layer
    enabled_layer = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)

    return enabled_layer


def render_layer_names_cmds():
    # Return render layer names without the "rs_" prefix
    render_layer_names = cmds.renderSetup(q=True, renderLayers=True)
    return render_layer_names


def currently_enabled_layer():
    # Get the currently enabled render layer
    enabled_layer = renderLayer.RenderLayer.findCurrentRenderLayer()

    return enabled_layer


def layer_object_from_layer_name():
    # if the specified layer does not exist, renderSetup returns error
    # so using try statement
    layer_name = get_currently_enabled_layer_name()
    try:
        render_layer = renderSetup.instance().getRenderLayer(layer_name)
        return render_layer
    except:
        return None


def main():
    """docstring for main"""
    # Call the function to get the currently enabled layer
    enabled_layer = currently_enabled_layer()

    # Print the name of the currently enabled layer
    print("Currently enabled layer:", enabled_layer.name() if enabled_layer else "No enabled layer found.")


if __name__ == '__main__':
    main()
