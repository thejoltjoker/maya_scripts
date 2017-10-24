allTextures = cmds.ls(tex=True)

for texture in allTextures:
    if cmds.nodeType(texture) == 'file':
        texturePath = cmds.getAttr(texture + ".fileTextureName")

        print texture + " = " + texturePath
