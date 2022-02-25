#!/usr/bin/env python
"""
make_obj_id_annotations.py
Description of make_obj_id_annotations.py.
"""
from maya import cmds


def main():
    """docstring for main"""

    sel = cmds.ls(sl=True)
    for i in sel:
        # Get object id
        obj_id = cmds.getAttr(i+'.rsObjectId')
        obj_world_pos = cmds.xform(q=True, ws=True, t=True)
        print( obj_world_pos)
        # obj_annotation = cmds.annotate(i, tx='my annotation text', p=obj_world_pos)
        obj_annotation = cmds.particle(p=obj_world_pos)
        cmds.setAttr(obj_annotation[1]+'.particleRenderType', 2)
        cmds.addAttr(obj_annotation[1], ln='annObjectId')
        cmds.addAttr -is true -dt "string" -ln "attributeName" particleShape3;
        cmds.setAttr -type "string" particleShape3.attributeName "particleId";
        # obj_annotation_transform = cmds.listRelatives(obj_annotation, p=True)
        # cmds.setAttr(obj_annotation+'.displayArrow', 0)
        cmds.setAttr(obj_annotation[1]+'.overrideEnabled', 1)
        cmds.setAttr(obj_annotation[1]+'.overrideDisplayType', 2)
        cmds.setAttr(obj_annotation[1]+'.annObjectId', obj_id)

        cmds.parent(obj_annotation[0], i)

if __name__ == '__main__':
    main()
