import maya.cmds as cmds

allTextures = cmds.ls(tex=True)

for texture in allTextures:
    if cmds.nodeType(texture) == 'file':
        texturePath = cmds.getAttr(texture+".fileTextureName")
        cmds.setAttr(texture+".fileTextureName", texturePath, type='string')

        print "Reloaded "+texture+" with "+texturePath