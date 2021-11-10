"""
redshift_mattes.py
"""
import logging

import maya.cmds as cmds
import maya.mel as mel
import random

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def test_renderer():
    if cmds.getAttr("defaultRenderGlobals.currentRenderer") != 'redshift':
        cmds.warning("Redshift is not current renderer")
        return False
    else:
        cmds.setAttr('redshiftOptions.imageFormat', 1)
        print("Image format set to exr.")


def get_next_obj_id():
    """Get the next object id based on the already existing ones"""
    existing_ids = get_all_obj_ids()
    return max(existing_ids) + 1


def get_all_obj_ids():
    """Get all object ids in the scene"""
    nodes = cmds.ls()
    obj_ids = []

    for node in nodes:
        # Look for attribute and append it
        try:
            obj_id = cmds.getAttr(node + '.rsObjectId')
            obj_ids.append(obj_id)
        except Exception as e:
            logging.debug(e)
            pass

    return obj_ids


def get_all_mat_ids():
    """Get all object ids in the scene"""
    nodes = cmds.ls()
    mat_ids = []

    for node in nodes:
        # Look for attribute and append it
        try:
            mat_id = cmds.getAttr(node + '.rsMaterialId')
            mat_ids.append(mat_id)
        except Exception as e:
            logging.debug(e)
            pass

    return mat_ids


def assign_obj_id(node):
    """"Assign object id to a node"""
    obj_id = get_next_obj_id()

    if cmds.nodeType(node) == 'RedshiftObjectId':
        cmds.setAttr(node + '.objectId', obj_id)
        logging.info('Assigned obj id {0} to {1}'.format(cmds.getAttr(node + '.objectId'), node))
    else:
        shapes = cmds.listRelatives(node, shapes=True)
        cmds.setAttr(shapes[0] + '.rsObjectId', obj_id)
        logging.info('Assigned obj id {0} to {1}'.format(cmds.getAttr(shapes[0] + '.objectId'), shapes[0]))


def assign_obj_ids():
    for node in cmds.ls(sl=True):
        assign_obj_id(node)


def all_puzzle_mattes():
    mattes = []
    for node in cmds.ls(type='RedshiftAOV'):
        if cmds.getAttr(node + '.aovType') == 'Puzzle Matte':
            mattes.append(node)
    return mattes


def obj_ids_in_puzzle_mattes():
    obj_ids = []
    for node in all_puzzle_mattes():
        obj_ids.append(cmds.getAttr(node + '.redId'))
        obj_ids.append(cmds.getAttr(node + '.greenId'))
        obj_ids.append(cmds.getAttr(node + '.blueId'))
    return list(dict.fromkeys(obj_ids))


def puzzle_matte_channels():
    mattes = {}
    for node in all_puzzle_mattes():
        mattes[node] = {'.redId': cmds.getAttr(node + '.redId'),
                        '.greenId': cmds.getAttr(node + '.greenId'),
                        '.blueId': cmds.getAttr(node + '.blueId')}
    return mattes


def empty_puzzle_matte_channels():
    mattes = puzzle_matte_channels()
    empty_channels = {}
    for node, channels in mattes.items():
        for attr in channels:
            if attr == 0:
                empty_channels[node] = attr

    return empty_channels


def assign_mattes_to_obj_ids():
    mattes = puzzle_matte_channels()

    empty_channels = empty_puzzle_matte_channels()
    for obj_id in get_all_obj_ids():
        pass


def assigned_obj_ids():
    assigned_ids = []
    for k, v in puzzle_matte_channels().items():
        pass


# def createPuzzleMattes():
#     all_nodes = cmds.ls()
#     id_number = 1
#     inc = 1
#     current_ids = []
#     puzzle_cur_ids = []
#     puzzle_mattes = []
#     empty_puzzle_channels = []
#     empty_puzzle_channels_value = []
#     puzzle_id_channels = []
#     puzzle_channels = []
#     puzzle_channels_value = []
#
#     # Make list of puzzle mattes
#     existing_aovs = cmds.ls(type='RedshiftAOV')
#     for aov_node in existing_aovs:
#         # Get aov type
#         aov_nice = cmds.getAttr(aov_node + '.aovType')
#
#         # If the AOV is puzzle matte
#         if aov_nice == 'Puzzle Matte':
#             print
#             "aov_nice MATTE = " + aov_node
#
#             # Append to list of puzzle mattes
#             puzzle_mattes.append(aov_node)
#
#             red_id = cmds.getAttr(aov_node + '.redId')
#             if red_id == 0:
#                 # Add attribute to list of empty puzzle id channels
#                 empty_puzzle_channels.append(aov_node + '.redId')
#                 # Add value to list of empty puzzle id channels
#                 empty_puzzle_channels_value.append(cmds.getAttr(aov_node + '.redId'))
#             else:
#                 # Add attribute to list of puzzle id channels
#                 puzzle_channels.append(aov_node + '.redId')
#                 # Add value to list of puzzle id channels
#                 puzzle_channels_value.append(cmds.getAttr(aov_node + '.redId'))
#
#             green_id = cmds.getAttr(aov_node + '.greenId')
#             if green_id == 0:
#                 # Add attribute to list of empty puzzle id channels
#                 empty_puzzle_channels.append(aov_node + '.greenId')
#                 # Add value to list of empty puzzle id channels
#                 empty_puzzle_channels_value.append(cmds.getAttr(aov_node + '.greenId'))
#
#             else:
#                 # Add attribute to list of puzzle id channels
#                 puzzle_channels.append(aov_node + '.greenId')
#                 # Add value to list of puzzle id channels
#                 puzzle_channels_value.append(cmds.getAttr(aov_node + '.greenId'))
#
#             blue_id = cmds.getAttr(aov_node + '.blueId')
#             if blue_id == 0:
#                 # Add attribute to list of empty puzzle id channels
#                 empty_puzzle_channels.append(aov_node + '.blueId')
#                 # Add value to list of empty puzzle id channels
#                 empty_puzzle_channels_value.append(cmds.getAttr(aov_node + '.blueId'))
#
#             else:
#                 # Add attribute to list of puzzle id channels
#                 puzzle_channels.append(aov_node + '.blueId')
#                 # Add value to list of puzzle id channels
#                 puzzle_channels_value.append(cmds.getAttr(aov_node + '.blueId'))
#
#     for i in empty_puzzle_channels:
#         print
#         "empty_puzzle_channels = " + str(i)
#     for i in empty_puzzle_channels_value:
#         print
#         "empty_puzzle_channels_value = " + str(i)
#
#     for i in puzzle_channels:
#         print
#         "puzzle_channels = " + str(i)
#     for i in puzzle_channels_value:
#         print
#         "puzzle_channels_value = " + str(i)
#
#     count_empty_puzzle_channels = len(empty_puzzle_channels)
#
#     # Loop through all nodes and check for object ids
#     for node in all_nodes:
#         id_exists = cmds.attributeQuery('rsObjectId', node=node, exists=True)
#         if id_exists:
#             # If object id exists
#             current_obj_id = cmds.getAttr(node + '.rsObjectId')
#             if current_obj_id != 0:
#
#                 # Check if a puzzle matte already contains the id
#                 if current_obj_id in puzzle_channels_value:
#                     print
#                     "There is already a Puzzle Matte for " + str(current_obj_id)
#                 else:
#                     # Check if there's an empty puzzle matte channel
#                     if count_empty_puzzle_channels != 0:
#                         cmds.setAttr(empty_puzzle_channels[0], current_obj_id)
#                         empty_puzzle_channels.remove(empty_puzzle_channels[0])
#                         # print str(empty_puzzle_channels[0])+" was assigned object id "+str(current_obj_id)
#                     else:
#                         # Test for puzzle matte name
#                         puzzle_name = 'ObjectId'
#                         puzzle_increment = str(inc)
#                         new_puzzle_increment = puzzle_increment.zfill(2)
#                         new_puzzle_name = "_".join([puzzle_name, new_puzzle_increment])
#                         for n in puzzle_mattes:
#                             if n != new_puzzle_name:
#                                 print
#                                 "NEW NAME"
#                                 inc += 1
#                                 puzzle_increment = str(inc)
#                                 new_puzzle_increment = puzzle_increment.zfill(2)
#                                 new_puzzle_name = "_".join([puzzle_name, new_puzzle_increment])
#
#                         aov_node = cmds.rsCreateAov(type='Puzzle Matte')
#                         cmds.setAttr(aov_node + '.mode', 1)
#                         cmds.setAttr(aov_node + '.name', new_puzzle_name, type='string')
#                         cmds.setAttr(aov_node + '.filePrefix', '<BeautyPath>/<BeautyFile>', type='string')
#                         cmds.setAttr(aov_node + '.redId', current_obj_id)
#
#                         # Append to list of puzzle mattes
#                         puzzle_mattes.append(aov_node)
#
#                         empty_puzzle_channels.append(aov_node + '.greenId')
#                         empty_puzzle_channels.append(aov_node + '.blueId')
#                         empty_puzzle_channels_value.append(cmds.getAttr(aov_node + '.greenId'))
#                         empty_puzzle_channels_value.append(cmds.getAttr(aov_node + '.blueId'))
#                         print
#                         empty_puzzle_channels
#                         count_empty_puzzle_channels = len(empty_puzzle_channels)
#
#     if cmds.frameLayout('rsLayout_AovAOVsFrame', exists=1):
#         mel.eval('redshiftUpdateActiveAovList')


if __name__ == '__main__':
    print(get_next_obj_id())
    print(get_all_obj_ids())
    print(assign_obj_ids())
    print(all_puzzle_mattes())
    print(obj_ids_in_puzzle_mattes())
    print(puzzle_matte_channels())
    print(empty_puzzle_matte_channels())
    print(assign_mattes_to_obj_ids())
    print(assigned_obj_ids())
