import maya.cmds as cmds

selTextures = cmds.ls(sl=True)

astPath = 'GrimlockTrex'
verPath = 'v002'
sastPath = 'cha_grimlock_gs_mp08'
ostPath = 'P:'

for texture in selTextures:
    if cmds.nodeType(texture) == 'file':
        texturePath = cmds.getAttr(texture+".fileTextureName")
        ostTexturePath = texturePath.replace('${OSPATH}', ostPath)
        astTexturePath = ostTexturePath.replace('<ast>', astPath)
        verTexturePath = astTexturePath.replace('<ver>', verPath)
        sastTexturePath = verTexturePath.replace('<sast>', sastPath)
        cmds.setAttr(texture+".fileTextureName", sastTexturePath, type='string')

        print "Path changed from "+texturePath+" to "+sastTexturePath