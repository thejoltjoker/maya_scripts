import maya.cmds as cmds
def plane_to_point():
    sel_nodes = cmds.ls(sl=True)

    extrusion_group = cmds.group(em=True, name='extruded_GRP')

    for node in sel_nodes:
        # Get position of first cv
        curve_point = cmds.pointPosition(node+'.cv[0]')
        ppos_x = float(curve_point[0])
        ppos_y = float(curve_point[1])
        ppos_z = float(curve_point[2])

        # Create plane
        extrude_plane = cmds.polyPlane(sx=1, sy=1, w=.16, h=.16)
        cmds.setAttr(extrude_plane[0]+'.translateX', ppos_x)
        cmds.setAttr(extrude_plane[0]+'.translateY', ppos_y)
        cmds.setAttr(extrude_plane[0]+'.translateZ', ppos_z)

        # Extrude plane
        extrusion = cmds.polyExtrudeFacet(extrude_plane[0]+'.f[0]', divisions=300, inputCurve=node)
        cmds.polyNormal(extrude_plane[0], normalMode=0)

        # Clean up
        final_extrusion = cmds.rename(extrude_plane[0], node+'Extruded')
        cmds.parent(final_extrusion, extrusion_group)
