#!/usr/bin/env python3
"""beaver.py
Project specific script for "beaver"
"""
import random
import sys

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
    try:
        main = cmds.parent(main, container)
    except:
        pass
    groups[name] = main
    # Children
    children = ['geo', 'light']
    for child in children:
        group_name = f'{name}_{child}_grp'
        group = cmds.ls(group_name)
        if not group:
            group = cmds.group(name=group_name, em=True)
        try:
            group = cmds.parent(group, main)
        except:
            pass
        groups[child] = group
    return groups


def create_sets(name):
    cmds.select(clear=True)
    set_names = ['include', 'exclude', 'light']
    nodes = []
    sets = {}
    for s in set_names:
        node = crl.get_or_create_set(f'{name}_{s}_set')
        nodes.append(node)
        sets[s] = node

    container = crl.get_or_create_set(f'{name}_set', nodes)
    return sets


def remove_suffix(input_string, separator='_'):
    split_string = input_string.split(separator)
    if len(split_string) > 1:
        split_string = split_string[:-1]
    return separator.join(split_string)


def create_cube():
    """Create group and layer
    """
    selection = cmds.ls(sl=True)
    if sys.platform == 'darwin':
        # TEMP SETUP
        name = 'beaver'
        cmds.file('/Users/johannes/Desktop/temp/test.ma', o=True, f=True)
        # cmds.file(new=True, f=True)
        # name = 'beaver'
        # cmds.group(n='groups_grp', em=True)
        # camera = cmds.camera()
        # cmds.rename(camera[0], 'renderCam_cam')
        cmds.select('pCube1')
        # END TEMP SETUP

    else:
        name = dialog_prompt(message='Enter name of group/layer:')

    if name:
        # Create groups
        groups = create_groups(name)
        sets = create_sets(name)
        env_set = crl.get_or_create_set('env_set')

        # Create redshift visibility node or select if already exists
        cmds.select(groups.get('geo'), r=True)
        visibility_node_name = f'{remove_suffix(groups.get("geo")[0])}_rsVisibility'
        visibility_node = cmds.ls(visibility_node_name)
        if not visibility_node:
            visibility_node = mel.eval('redshiftCreateVisibilityNode();')
            visibility_node = cmds.rename(visibility_node, visibility_node_name)
        else:
            visibility_node = visibility_node[0]

        # Copy light setup
        lights_group = cmds.duplicate('template_lights_grp', renameChildren=True)[0]
        lights_nodes = cmds.listRelatives(lights_group, allDescendents=True)
        for node in lights_nodes:
            cmds.rename(node, node.replace('template', name).rstrip('1'))

        # Ugly workaround
        cmds.delete(groups['light'])
        lights_group = cmds.rename(lights_group, groups['light'])
        cmds.parent(lights_group, groups[name])

        # Put selection in geo group
        cmds.select(clear=True)
        try:
            cmds.parent(selection, groups.get('geo'))
        except:
            pass

        # Create render setup instance
        rs = crl.render_setup_instance()

        # Create beauty render layer
        layer_name = f'{name}_beauty'

        layer = crl.get_or_create_layer(rs, layer_name)

        # Create group
        group = crl.get_or_create_group(layer, f'{layer_name}_base_grp')

        # Create collections
        # Collection: include
        include_col = crl.get_or_create_collection(group, f'{layer_name}_include')

        # include everything in set
        crl.set_collection_filters(include_col, filter_type=5, pattern=sets['include'])

        # Create subcollections
        # include_transform_col = crl.get_or_create_collection(include_col, f'{layer_name}_include_transform')
        # crl.set_collection_filters(include_transform_col, filter_type=1, pattern='*')
        # include_shapes_col = crl.get_or_create_collection(include_transform_col, f'{layer_name}_include_shape')
        # crl.set_collection_filters(include_shapes_col, filter_type=2, pattern='*')

        # Add geo to include set
        cmds.sets(groups['geo'], include=sets['include'])

        # Turn on primary visibility
        # crl.set_override(include_shapes_col, visibility_node, 'enableVisibilityOverrides', 1)
        # crl.set_override(include_shapes_col, visibility_node, 'primaryRayinclude', 1)

        # Collection: exclude
        exclude_col = crl.get_or_create_collection(group, f'{layer_name}_exclude')

        # exclude everything in set
        crl.set_collection_filters(exclude_col, filter_type=5, pattern=sets['exclude'])
        exclude_col.setSelfEnabled(0)


        # Collection: Light
        light_col = crl.get_or_create_collection(group, f'{layer_name}_light')
        crl.set_collection_filters(light_col, filter_type=1, pattern=sets['light'])

        # Add lights to set
        cmds.sets(groups['light'], include=sets['light'])


        # Collection: camera
        camera = 'renderCam_cam'
        camera_shape = cmds.listRelatives(camera, children=True)[0]
        camera_col = crl.get_or_create_collection(group, f'{layer_name}_cam')
        crl.set_collection_filters(camera_col, filter_type=8, pattern=camera_shape, custom_filter_type='camera')
        crl.set_override(camera_col, camera_shape, 'renderable', True)

        # Add general lights
        # lights_nodes = cmds.ls('primary_lights_grp', l=True)
        # lights_nodes.extend(groups.get('lights'))
        # print(lights_nodes)
        # crl.add_static_selection(lights_col, lights_nodes)

        # Set env overrides
        env_group = crl.get_or_create_group(group, f'{layer_name}_env')
        env_col = crl.get_or_create_collection(env_group, f'{layer_name}_env')
        cube_vis_node = cmds.ls('cube_rsVisibility', l=True)[0]
        vis_nodes = cmds.ls('cube_geo', l=True)
        vis_nodes.append(cube_vis_node)
        crl.set_collection_filters(env_col, filter_type=5, pattern=env_set)

        vis_env_col = crl.get_or_create_collection(env_group, f'{layer_name}_env_visibility')
        crl.set_collection_filters(vis_env_col, filter_type=5, pattern=cube_vis_node)
        crl.set_override(vis_env_col, cube_vis_node, 'enable', 1)
        crl.set_override(vis_env_col, cube_vis_node, 'primaryRayVisible', 0)


        # Shadow layer
        shadow_layer_name = f'{name}_shadow'

        layer = crl.get_or_create_layer(rs, shadow_layer_name)

        # Create group
        group = crl.get_or_create_group(layer, f'{shadow_layer_name}_base_grp')

        # Create collections
        # Collection: include
        include_col = crl.get_or_create_collection(group, f'{shadow_layer_name}_include')

        # include everything in set
        crl.set_collection_filters(include_col, filter_type=5, pattern=sets['include'])

        # Turn off primary visibility
        vis_geo_col = crl.get_or_create_collection(group, f'{shadow_layer_name}_geo_visibility')
        crl.set_collection_filters(vis_geo_col, filter_type=5, pattern=visibility_node)
        crl.set_override(vis_geo_col, visibility_node, 'enable', 1)
        crl.set_override(vis_geo_col, visibility_node, 'primaryRayVisible', 0)


        # Collection: exclude
        exclude_col = crl.get_or_create_collection(group, f'{shadow_layer_name}_exclude')

        # exclude everything in set
        crl.set_collection_filters(exclude_col, filter_type=5, pattern=sets['exclude'])
        exclude_col.setSelfEnabled(0)

        # Collection: Light
        light_col = crl.get_or_create_collection(group, f'{shadow_layer_name}_light')
        crl.set_collection_filters(light_col, filter_type=1, pattern=cmds.ls('primary_lights_grp', l=True)[0])


        # Collection: camera
        camera = 'renderCam_cam'
        camera_shape = cmds.listRelatives(camera, children=True)[0]
        camera_col = crl.get_or_create_collection(group, f'{shadow_layer_name}_cam')
        crl.set_collection_filters(camera_col, filter_type=8, pattern=camera_shape, custom_filter_type='camera')
        crl.set_override(camera_col, camera_shape, 'renderable', True)


        # Set env overrides
        env_group = crl.get_or_create_group(group, f'{shadow_layer_name}_env')
        env_col = crl.get_or_create_collection(env_group, f'{shadow_layer_name}_env')
        cube_vis_node = cmds.ls('cube_rsVisibility', l=True)[0]
        vis_nodes = cmds.ls('cube_geo', l=True)
        vis_nodes.append(cube_vis_node)
        crl.set_collection_filters(env_col, filter_type=5, pattern=env_set)

        vis_env_col = crl.get_or_create_collection(env_group, f'{shadow_layer_name}_env_visibility')
        crl.set_collection_filters(vis_env_col, filter_type=5, pattern=cube_vis_node)
        crl.set_override(vis_env_col, cube_vis_node, 'enable', 1)
        crl.set_override(vis_env_col, cube_vis_node, 'primaryRayVisible', 1)

        matte_env_col = crl.get_or_create_collection(env_group, f'{shadow_layer_name}_env_matte')
        cube_matte_params = 'cube_rsMatteParameters'
        crl.set_collection_filters(matte_env_col, filter_type=5, pattern=cube_matte_params)
        crl.set_override(matte_env_col, cube_matte_params, 'matteEnable', 1)
        # # Create layer
        # shadow_layer = crl.get_or_create_layer(rs, shadow_layer_name)
        #
        # # Create collection for geometry
        # include_col = crl.get_or_create_collection(shadow_layer, f'{shadow_layer_name}_include')
        # include_sets_col = crl.get_or_create_collection(include_col, f'{layer_name}_visibility')
        # crl.set_collection_filters(include_sets_col, filter_type=5, pattern=visibility_node)
        # crl.set_override(include_sets_col, visibility_node, 'enable', 1)
        # crl.set_override(include_sets_col, visibility_node, 'primaryRayVisible', 1)
        #
        # # Create collection for parameters
        # params_col = crl.get_or_create_collection(shadow_layer, f'{shadow_layer_name}_params')
        #
        # # List of nodes to include
        # shadow_nodes = cmds.ls('cube_geo', l=True)
        # shadow_nodes.extend(cmds.ls('primary_lights_grp', l=True))
        # shadow_nodes.extend(cmds.ls(groups.get('geo'), l=True))
        # crl.add_static_selection(include_col, shadow_nodes)
        #
        # # Add nodes to collections


        #
        # # Subcollection for sets
        # include_sets_col = crl.get_or_create_collection(shadow_layer, f'{shadow_layer_name}_visibility')
        # crl.set_collection_filters(include_sets_col, filter_type=5, pattern=visibility_node)
        # crl.set_override(include_sets_col, visibility_node, 'enable', 1)
        # crl.set_override(include_sets_col, visibility_node, 'primaryRayVisible', 0)
        #
        # if cmds.ls('rsAOVControl'):
        #     aovs_col = crl.get_or_create_collection(shadow_layer, f'{shadow_layer_name}_aovs')
        #     crl.set_collection_filters(aovs_col, filter_type=1, pattern='rsAOVControl')
        #     crl.set_override(aovs_col, 'rsAOVControl', 'enableBeauty', 0)
        #     crl.set_override(aovs_col, 'rsAOVControl', 'enableRawBeauty', 0)
        #     crl.set_override(aovs_col, 'rsAOVControl', 'enableUtility', 0)


def main():
    """docstring for main"""
    create_cube()


if __name__ == '__main__':
    main()
