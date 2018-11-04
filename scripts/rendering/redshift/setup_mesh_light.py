#!/usr/bin/env python
"""
setup_mesh_light.py
Description of setup_mesh_light.py.
"""
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om


def main():
    """Creates a light, converts it to a mesh light, constrains to and hides the original mesh."""
    # Get only geometry from selection
    sel = [
        x for x in cmds.ls(sl=True)
        if cmds.listRelatives(x)
        if cmds.nodeType(cmds.listRelatives(x)[0]) == 'mesh'
    ]

    if sel:
        for obj in sel:
            # Create light
            mel.eval('redshiftCreateLight "RedshiftPhysicalLight";')
            new_light = cmds.ls(sl=True)[0]
            light = cmds.rename(new_light, '{}Light_LGT'.format(obj))
            shape = cmds.listRelatives(light)[0]

            # Set light to mesh light
            cmds.setAttr('{}.areaShape'.format(shape), 4)

            # Attach mesh to light
            cmds.select(obj, light)
            mel.eval(
                'AERedshiftPhysicalLightTemplate_areaShapeObject_link {}.areaShapeObject'.
                format(shape))

            # Constrain light to geometry
            cmds.parentConstraint(obj, light, w=1)
            cmds.scaleConstraint(obj, light, w=1)

            # Hide original mesh
            cmds.setAttr('{}.visibility'.format(obj), 0)
    else:
        om.MGlobal.displayWarning("No meshes selected.")


if __name__ == '__main__':
    main()
