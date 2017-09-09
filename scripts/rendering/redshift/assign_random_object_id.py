#!/usr/bin/env python
"""
assign_random_object_id.py
Description of assign_random_object_id.py.
"""
import maya.cmds as cmds
from random import randint
def assign_random_obj_id():
    """docstring for assign_random_ob_id"""
    random_id = randint(0, 9999)
    sel = cmds.ls(sl=True)
    obj = sel[0]

    if cmds.nodeType(obj) == 'RedshiftObjectId':
        print 'objid object'
        cmds.setAttr(obj+'.objectId', random_id)
        print obj + ' = ' + str(cmds.getAttr(obj+'.objectId'))
    else:
        obj_list = cmds.listRelatives(sel[0], shapes=True)
        obj = obj_list[0]
        cmds.setAttr(obj+'.rsObjectId', random_id)
        print obj + ' = ' + str(cmds.getAttr(obj+'.rsObjectId'))


if __name__ == '__main__':
    assign_random_obj_id()

# shape =
# rsObjectId
