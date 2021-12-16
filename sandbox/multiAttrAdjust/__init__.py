import maya.cmds as cmds
from functools import partial


class multiAttrAdjust(object):
    def __init__(self, *args):
        super(multiAttrAdjust, self).__init__(*args)

        # Define an id string for the window first
        winID = 'attrAdjustWindow'

        # Test to make sure that the UI isn't already active
        if cmds.window(winID, exists=True):
            cmds.deleteUI(winID)

        self.window = cmds.window(winID, t='Change multiple attribute values')
        self.layout = cmds.columnLayout(w=200, rowSpacing=10, parent=self.window)

        # Add controls into this Layout
        cmds.text(label='Value', align='left', parent=self.layout)
        valInput = cmds.floatField(w=200, parent=self.layout)
        cmds.text(label='Attribute', align='left', parent=self.layout)
        attrInput = cmds.textField(w=200, parent=self.layout)
        cmds.button(label='update', command=self.changeValue, w=200, parent=self.layout)

        # Display the window
        cmds.showWindow()

    def changeValue(self, valInput, attrInput, svalInput, *args):

        selNodes = cmds.ls(sl=True)

        valOutput = cmds.floatField(valInput, query=True, text=True)
        attrOutput = cmds.textField(attrInput, query=True, text=True)

        for texture in selTextures:
            cmds.setAttr(attrOutput, valOutput)

    def test(self):
        cmds.warning("SUCCESS")
