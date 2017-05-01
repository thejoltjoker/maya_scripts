"""
rs_create_puzzle_mattes.py
"""
import maya.cmds as cmds
import maya.mel as mel

def testRenderer():
    if cmds.getAttr("defaultRenderGlobals.currentRenderer") != 'redshift':
        cmds.warning("Redshift is not current renderer")
        return False
    else:
        cmds.setAttr('redshiftOptions.imageFormat', 1)
        print "Image format set to exr."

def createPuzzleMattes():
    all_nodes = cmds.ls()
    id_number = 1
    inc = 1
    current_ids = []
    puzzle_cur_ids = []
    puzzle_mattes = []
    empty_puzzle_channels = []
    empty_puzzle_channels_value = []
    puzzle_id_channels = []
    puzzle_channels = []
    puzzle_channels_value = []

    # Make list of puzzle mattes
    existing_aovs = cmds.ls(type='RedshiftAOV')
    for aov_node in existing_aovs:
        # Get aov type
        aov_nice = cmds.getAttr(aov_node+'.aovType')

        # If the AOV is puzzle matte
        if aov_nice == 'Puzzle Matte':
            print "aov_nice MATTE = "+aov_node

            # Append to list of puzzle mattes
            puzzle_mattes.append(aov_node)

            red_id = cmds.getAttr(aov_node+'.redId')
            if red_id == 0:
                # Add attribute to list of empty puzzle id channels
                empty_puzzle_channels.append(aov_node+'.redId')
                # Add value to list of empty puzzle id channels
                empty_puzzle_channels_value.append(cmds.getAttr(aov_node+'.redId'))
            else:
                # Add attribute to list of puzzle id channels
                puzzle_channels.append(aov_node+'.redId')
                # Add value to list of puzzle id channels
                puzzle_channels_value.append(cmds.getAttr(aov_node+'.redId'))

            green_id = cmds.getAttr(aov_node+'.greenId')
            if green_id == 0:
                # Add attribute to list of empty puzzle id channels
                empty_puzzle_channels.append(aov_node+'.greenId')
                # Add value to list of empty puzzle id channels
                empty_puzzle_channels_value.append(cmds.getAttr(aov_node+'.greenId'))

            else:
                # Add attribute to list of puzzle id channels
                puzzle_channels.append(aov_node+'.greenId')
                # Add value to list of puzzle id channels
                puzzle_channels_value.append(cmds.getAttr(aov_node+'.greenId'))

            blue_id = cmds.getAttr(aov_node+'.blueId')
            if blue_id == 0:
                # Add attribute to list of empty puzzle id channels
                empty_puzzle_channels.append(aov_node+'.blueId')
                # Add value to list of empty puzzle id channels
                empty_puzzle_channels_value.append(cmds.getAttr(aov_node+'.blueId'))

            else:
                # Add attribute to list of puzzle id channels
                puzzle_channels.append(aov_node+'.blueId')
                # Add value to list of puzzle id channels
                puzzle_channels_value.append(cmds.getAttr(aov_node+'.blueId'))

    for i in empty_puzzle_channels:
        print "empty_puzzle_channels = "+str(i)
    for i in empty_puzzle_channels_value:
        print "empty_puzzle_channels_value = "+str(i)

    for i in puzzle_channels:
        print "puzzle_channels = "+str(i)
    for i in puzzle_channels_value:
        print "puzzle_channels_value = "+str(i)

    count_empty_puzzle_channels = len(empty_puzzle_channels)

    # Loop through all nodes and check for object ids
    for node in all_nodes:
        id_exists = cmds.attributeQuery('rsObjectId', node=node, exists=True)
        if id_exists:
            # If object id exists
            current_obj_id = cmds.getAttr(node+'.rsObjectId')
            if current_obj_id != 0:

                # Check if a puzzle matte already contains the id
                if current_obj_id in puzzle_channels_value:
                    print "There is already a Puzzle Matte for "+str(current_obj_id)
                else:
                    # Check if there's an empty puzzle matte channel
                    if count_empty_puzzle_channels != 0:
                        cmds.setAttr(empty_puzzle_channels[0], current_obj_id)
                        empty_puzzle_channels.remove(empty_puzzle_channels[0])
                        # print str(empty_puzzle_channels[0])+" was assigned object id "+str(current_obj_id)
                    else:
                        # Test for puzzle matte name
                        puzzle_name = 'ObjectId'
                        puzzle_increment = str(inc)
                        new_puzzle_increment = puzzle_increment.zfill(2)
                        new_puzzle_name = "_".join([puzzle_name, new_puzzle_increment])
                        for n in puzzle_mattes:
                            if n != new_puzzle_name:
                                print "NEW NAME"
                                inc += 1
                                puzzle_increment = str(inc)
                                new_puzzle_increment = puzzle_increment.zfill(2)
                                new_puzzle_name = "_".join([puzzle_name, new_puzzle_increment])

                        aov_node = cmds.rsCreateAov(type='Puzzle Matte')
                        cmds.setAttr(aov_node+'.mode', 1)
                        cmds.setAttr(aov_node+'.name', new_puzzle_name, type='string')
                        cmds.setAttr(aov_node+'.filePrefix', '<BeautyPath>/<BeautyFile>', type='string')
                        cmds.setAttr(aov_node+'.redId', current_obj_id)

                        # Append to list of puzzle mattes
                        puzzle_mattes.append(aov_node)

                        empty_puzzle_channels.append(aov_node+'.greenId')
                        empty_puzzle_channels.append(aov_node+'.blueId')
                        empty_puzzle_channels_value.append(cmds.getAttr(aov_node+'.greenId'))
                        empty_puzzle_channels_value.append(cmds.getAttr(aov_node+'.blueId'))
                        print empty_puzzle_channels
                        count_empty_puzzle_channels = len(empty_puzzle_channels)

    if cmds.frameLayout('rsLayout_AovAOVsFrame', exists=1):
        mel.eval('redshiftUpdateActiveAovList')


createPuzzleMattes()