import maya.cmds as cmds

cmds.headsUpDisplay( 'HUDObjectId', rem=True )

def objectId(*args):
    try:
        sel_nodes = cmds.ls(sl=True)
        sel_shape = cmds.listRelatives(sel_nodes[0], shapes=True)
        obj_id = cmds.getAttr('%s.rsObjectId' % sel_shape[0])
        print sel_shape[0]
        print obj_id
        return obj_id
    except:
        return 0
#
#Now, create a HUD object to display the return value of the above procedure
#
#Attributes:
#
#        - Section 1, block 0, represents the top second slot of the view.
#        - Set the blockSize to "medium", instead of the default "small"
#        - Assigned the HUD the label: "Position"
#        - Defined the label font size to be large
#        - Assigned the HUD a command to run on a SelectionChanged trigger
#        - Attached the attributeChange node change to the SelectionChanged trigger
#          to allow the update of the data on attribute changes.
#

cmds.headsUpDisplay( 'HUDObjectId', section=1, block=1, blockSize='medium', label='Object ID', labelFontSize='large', command=objectId, event='SelectionChanged', nodeChanges='attributeChange' )



def objectPosition(*args):
        try:
                selectedNodes = cmds.selectedNodes()
                mainObj = selectedNodes[-1]
                positionList = cmds.getAttr('%s.translate' % mainObj)
                return positionList[0]
        except:
                return (0.0,0.0,0.0)
#Attributes:
#
#        - Section 1, block 0, represents the top second slot of the view.
#        - Assigned the HUD a command to run on a SelectionChanged trigger
#        - Attached the attributeChange node change to the SelectionChanged trigger
#          to allow the update of the data on attribute changes.
#
cmds.headsUpDisplay( 'HUDObjectPosition', section=1, block=1, blockSize='medium', label='Position', labelFontSize='large', command=objectPosition, event='SelectionChanged', nodeChanges='attributeChange' )