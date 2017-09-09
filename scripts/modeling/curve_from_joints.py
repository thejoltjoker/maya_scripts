"""
curve_from_joints.py

Creates a curve from the select joint chain.
"""
import maya.cmds as cmds

sel_nodes = cmds.ls(sl=True)
joint_positions = []
control_point_list = []
if sel_nodes:
    joint_children = cmds.listRelatives(children=True, allDescendents=True)

    joint_children.append(sel_nodes[0])
    joint_children.reverse()
    print joint_children

    for joint_id, joint_name in enumerate(joint_children):

        world_space = cmds.xform(joint_name, q=True, t=True, ws=True)
        world_space_vector = (world_space[0], world_space[1], world_space[2])
        joint_positions.append(world_space_vector)

        control_point_list.append(joint_id)

cmds.curve(d=1, p=joint_positions)
