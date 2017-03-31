"""
assignRedshiftIds.py

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

assignRedshiftIds()




# DON'T MIND THIS....

# shading_groups = cmds.listConnections(sel_nodes, type='shadingEngine')
# remove duplicate shading groups from list
# shadingGrps = list(set(shadingGrps))

# .rsMaterialId" 1;