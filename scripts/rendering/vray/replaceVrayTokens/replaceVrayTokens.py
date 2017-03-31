"""
replaceVrayTokens.py

Replace filename tokens in your texture path. Basically a glorified search and replace.
"""
from functools import partial
import maya.cmds as cmds

class replaceVrayToken(object):
    """docstring for replaceVrayToken"""
    def __init__(self):
        super(replaceVrayToken, self).__init__()
        # Define an id string for the window first
        winID = 'vrayTokenWindow'

        # Test to make sure that the UI isn't already active
        if cmds.window(winID, exists=True):
            cmds.deleteUI(winID)

        self.window = cmds.window(winID, t='Replace Vray Tokens')
        self.layout = cmds.columnLayout(w=200, rowSpacing=10, parent=self.window)

        # Add controls into this Layout
        cmds.text(label='<ast>', align='left', parent=self.layout)
        astInput = cmds.textField(w=200, parent=self.layout)
        cmds.text(label='<ver>', align='left', parent=self.layout)
        verInput = cmds.textField(w=200, parent=self.layout)
        cmds.text(label='<sast>', align='left', parent=self.layout)
        sastInput = cmds.textField(w=200, parent=self.layout)
        cmds.button(label='replace', command=partial(self.replaceFileName,astInput,verInput,sastInput), w=200, parent=self.layout)
        cmds.button(label='cancel', command=cmds.deleteUI(winID), w=200, parent=self.layout)

        # Display the window
        cmds.showWindow()

    def replaceFileName(self, astInput, verInput, sastInput,*args):
        selTextures = cmds.ls(sl=True)

        for texture in selTextures:
            if cmds.nodeType(texture) == 'file':
                texturePath = cmds.getAttr(texture+".fileTextureName")
                astTexturePath = texturePath.replace('<ast>', astInput)
                verTexturePath = astTexturePath.replace('<ver>', verInput)
                sastTexturePath = verTexturePath.replace('<sast>', sastInput)
                cmds.setAttr(texture+".fileTextureName", sastTexturePath, type='string')

                print "Path changed from "+texturePath+" to "+sastTexturePath

    def printTexturePath(self, *args):
        selTextures = cmds.ls(sl=True)

        for texture in selTextures:
            if cmds.nodeType(texture) == 'file':
                texturePath = cmds.getAttr(texture+".fileTextureName")

                print texturePath

replaceVrayToken()