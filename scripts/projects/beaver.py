#!/usr/bin/env python3
"""beaver.py
Project specific script for "beaver"
"""
import random
from maya import cmds, mel
from maya_scripts.scripts.rendering import create_render_layers as crl
from importlib import reload

reload(crl)

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger()


def dialog_prompt(dialog_title='Dialog Window', message='Enter input:', default_button='OK', cancel_button='Cancel'):
    dialog = cmds.promptDialog(
        title=dialog_title,
        message=message,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            return output
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")

    return False


def create_groups(name, container='groups_grp'):
    groups = {}
    if not cmds.ls(container):
        container = cmds.group(name=container, em=True)
    # Main group
    main = cmds.ls(f'{name}_grp')
    if not main:
        main = cmds.group(name=f'{name}_grp', em=True)
    main = cmds.parent(main, container)
    groups[name] = main
    # Children
    children = ['geo', 'lights']
    for child in children:
        group_name = f'{name}_{child}_grp'
        group = cmds.ls(group_name)
        if not group:
            group = cmds.group(name=group_name, em=True)
        group = cmds.parent(group, main)
        groups[child] = group
    return groups


def remove_suffix(input_string, separator='_'):
    split_string = input_string.split(separator)
    if len(split_string) > 1:
        split_string = split_string[:-1]
    return separator.join(split_string)


def create_cube():
    """Create group and layer
    """
    name = dialog_prompt(message='Enter name of group/layer:')
    selection = cmds.ls(sl=True)
    # TEMP SETUP
    # cmds.file(new=True, f=True)
    # name = 'beaver'
    # cmds.group(n='groups_grp', em=True)
    # camera = cmds.camera()
    # cmds.rename(camera[0], 'renderCam_cam')
    # END TEMP SETUP
    if name:
        # Create groups
        groups = create_groups(name)
        cmds.select(groups.get('geo'), r=True)
        visibility_node_name = f'{remove_suffix(groups.get("geo")[0])}_rsVisibility'
        visibility_node = cmds.ls(visibility_node_name)
        if not visibility_node:
            visibility_node = mel.eval('redshiftCreateVisibilityNode();')
            visibility_node = cmds.rename(visibility_node, visibility_node_name)
        else:
            visibility_node = visibility_node[0]

        # Put selection in geo group
        cmds.select(clear=True)
        cmds.parent(selection, groups.get('geo'))

        # Create primary render layer
        layer_name = f'{name}_primary'

        # Create render setup instance
        rs = crl.render_setup_instance()

        # Get or create a layer
        layer = crl.get_or_create_layer(rs, layer_name)

        # Create group
        group = crl.get_or_create_group(layer, f'{layer_name}_base_grp')

        # Create collections
        include_col = crl.get_or_create_collection(group, f'{layer_name}_include')
        crl.set_collection_filters(include_col, filter_type=1, pattern=groups[name][0])

        # Subcollection for shapes
        include_shape_col = crl.get_or_create_collection(include_col, f'{layer_name}_include_shapes')
        crl.set_collection_filters(include_shape_col, filter_type=2)

        # Subcollection for sets
        include_sets_col = crl.get_or_create_collection(group, f'{layer_name}_visibility')
        crl.set_collection_filters(include_sets_col, filter_type=5, pattern=visibility_node)
        crl.set_override(include_sets_col, visibility_node, 'enable', 1)
        crl.set_override(include_sets_col, visibility_node, 'primaryRayVisible', 1)

        # Camera collection
        camera = 'renderCam_cam'
        camera_shape = cmds.listRelatives(camera, children=True)[0]
        camera_col = crl.get_or_create_collection(group, f'{layer_name}_cam')
        crl.set_collection_filters(camera_col, filter_type=8, pattern=camera_shape, custom_filter_type='camera')
        crl.set_override(camera_col, camera_shape, 'renderable', True)

        # Set bg matteparameters
        cube_matte_params = 'cube_rsMatteParameters'
        shadow_col = crl.get_or_create_collection(group, f'{layer_name}_shadow')
        crl.set_collection_filters(shadow_col, filter_type=0, pattern='')
        shadow_geo_col = crl.get_or_create_collection(shadow_col, f'{layer_name}_shadow_geo')
        crl.set_collection_filters(shadow_geo_col, filter_type=1, pattern='')
        crl.add_static_selection(shadow_geo_col, cmds.ls('cube_geo', l=True))

        shadow_matte_col = crl.get_or_create_collection(shadow_col, f'{layer_name}_shadow_matte')
        crl.set_collection_filters(shadow_matte_col, filter_type=5, pattern=cube_matte_params)
        crl.set_override(shadow_matte_col, cube_matte_params, 'matteEnable', 1)


def main():
    """docstring for main"""
    create_cube()


if __name__ == '__main__':
    main()
