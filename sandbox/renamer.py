#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    # Get selection
    sel = cmds.ls(sl=True)

    # Create a counter
    count = 1

    # check if single select
    if len(sel) > 1:
        sel_single = False
    else:
        sel_single = True

    # Loop through selected nodeects
    for node in sel:

        node_type = cmds.nodeType(node)

        new_name = 'newName'

        # Set suffix depending on the dropdown
        if suffixOutput == 'Auto':

            print "new_suffix dropdown is Auto"

            # Figure out what kind of transform node.
            if node_type == 'transform':
                node_geo = cmds.listRelatives(node, s=True)
                if node_geo is not None:
                    for shape in node_geo:
                        shape_type = cmds.nodeType(shape)
                        if shape_type == 'mesh':
                            new_suffix = 'GEO'
                        elif shape_type == 'locator':
                            new_suffix = 'LOC'
                        elif shape_type == 'RedshiftPhysicalLight':
                            new_suffix = 'LGT'
                        else:
                            new_suffix = shape_type
                else:
                    new_suffix = 'GRP'

            elif node_type == 'joint':
                new_suffix = 'JNT'

            elif node_type == 'file':
                new_suffix = 'FILE'

            elif node_type == 'instancer':
                new_suffix = 'INST'

            elif node_type == 'ikHandle':
                new_suffix = 'IK'

            elif node_type == 'blendColors':
                new_suffix = 'CLR'

            elif node_type == 'skinCluster':
                new_suffix = 'SKIN'

            elif node_type == 'ikEffector':
                new_suffix = 'EFF'

            elif node_type == 'condition':
                new_suffix = 'COND'

            # Constraints
            elif node_type == 'pointConstraint':
                if node_type != 'poleVectorConstraint':
                    new_suffix = 'pointCnst'

            elif node_type == 'pointConstraint':
                if node_type == 'poleVectorConstraint':
                    new_suffix = 'poleCnst'

            elif node_type == 'orientConstraint':
                new_suffix = 'orientCnst'

            elif node_type == 'parentConstraint':
                new_suffix = 'parentCnst'

            # Redshift nodeects
            elif node_type == 'RedshiftVisibility':
                new_suffix = 'rsVis'

            elif node_type == 'RedshiftPhysicalLight':
                new_suffix = 'LGT'

            elif node_type == 'RedshiftnodeectId':
                new_suffix = 'rsnodeId'

            elif node_type == 'RedshiftMeshParameters':
                new_suffix = 'rsMeshParams'

            elif node_type in ['RedshiftSubSurfaceScatter', 'RedshiftMaterial']:
                new_suffix = 'MTL'

            else:
                new_suffix = cmds.nodeType(node)

            print "new_suffix is " + new_suffix

            else:
                print "new_suffix is " + new_suffix
                print "the nodeType is " + node_type
                # node_geo = cmds.listRelatives(node, s=True)
                # for shape in node_geo:
                #     shape_type = cmds.nodeType(shape)
                #     print "the child nodeType is "+str(shape_type)

                # if single nodeect no increment number
                # if singleSelect == True:
                #     finalNewName = (newName + '_' + new_suffix)
                # else:
                #     finalNewName = (newName + str('%03d' % count) + '_' + new_suffix)
                # cmds.rename(node, finalNewName)
        else:
            print "Suffix is not checked."

        # If prefix is checked
        if checkPrefixOutput:
            print "Prefix is checked."
        else:
            print "Prefix is not checked."

        # Set final new name depending on input.

        # if single nodeect no increment number
        if singleSelect == True:
            finalNewName = (newName)
        else:
            finalNewName = (newName + str('%03d' % count))

        if checkSuffixOutput:
            finalNewName += str("_" + new_suffix)

        # Rename nodes
        cmds.rename(node, finalNewName)

        # Increment counter
        count += 1


if __name__ == '__main__':
    main()
