"""
rs_assignRedshiftIds.py

Assign Redshift object id's to selected objects.
"""
import maya.cmds as cmds

def assignRedshiftIds():
    all_nodes = cmds.ls()
    sel_nodes = cmds.ls(dag=True, o=True, s=True, sl=True)
    id_number = 1
    current_ids = []

    # Make list of current object id's
    for node in all_nodes:
        id_exists = cmds.attributeQuery('rsObjectId', node=node, exists=True)
        if id_exists:
            current_obj_id = cmds.getAttr(node+'.rsObjectId')
            current_ids.append(current_obj_id)

    # Set object id
    for node in sel_nodes:
        id_exists = cmds.attributeQuery('rsObjectId', node=node, exists=True)
        if id_exists:
            current_obj_id = cmds.getAttr(node+'.rsObjectId')
            if current_obj_id == 0:
                while id_number in current_ids:
                    id_number += 1
                cmds.setAttr(node+'.rsObjectId', id_number)
                current_ids.append(id_number)
                print node+" has the object id "+str(id_number)
            else:
                print node+" has the object id "+str(current_obj_id)

    # Set material id
    shading_groups = cmds.listConnections(sel_nodes, type='shadingEngine')
    shading_groups = list(set(shading_groups))

    # Make list of current material id's
    current_mtl_ids = []
    for node in shading_groups:
        id_exists = cmds.attributeQuery('rsObjectId', node=node, exists=True)
        if id_exists:
            current_obj_id = cmds.getAttr(node+'.rsObjectId')
            current_mtl_ids.append(current_obj_id)

    for node in shading_groups:
        if node != 'initialShadingGroup':
            id_exists = cmds.attributeQuery('rsMaterialId', node=node, exists=True)
            if id_exists:
                current_obj_id = cmds.getAttr(node+'.rsMaterialId')
                if current_obj_id == 0:
                    while id_number in current_mtl_ids:
                        id_number += 1
                    cmds.setAttr(node+'.rsMaterialId', id_number)
                    current_mtl_ids.append(id_number)
                    print node+" has the material id "+str(id_number)
                else:
                    print node+" has the material id "+str(current_obj_id)

def listRedshiftIds():
    all_nodes = cmds.ls()
    id_number = 1
    current_ids = []

    # Print object id's
    for node in all_nodes:
        id_exists = cmds.attributeQuery('rsObjectId', node=node, exists=True)
        if id_exists:
            current_obj_id = cmds.getAttr(node+'.rsObjectId')
            if current_obj_id != 0:
                current_ids.append(current_obj_id)
                print node+" has the object id "+str(current_obj_id)

    # Get materials
    shading_groups = cmds.listConnections(all_nodes, type='shadingEngine')
    shading_groups = list(set(shading_groups))

    # Print material id's
    current_mtl_ids = []
    for node in shading_groups:
        if node != 'initialShadingGroup':
            id_exists = cmds.attributeQuery('rsMaterialId', node=node, exists=True)
            if id_exists:
                current_obj_id = cmds.getAttr(node+'.rsMaterialId')
                if current_obj_id != 0:
                    current_obj_id = cmds.getAttr(node+'.rsMaterialId')
                    print node+" has the material id "+str(current_obj_id)