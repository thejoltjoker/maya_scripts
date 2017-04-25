import maya.cmds as cmds
import maya.mel as mel
aovNode = cmds.rsCreateAov(type='Puzzle Matte')
cmds.setAttr((aovNode+'.filePrefix'), '<BeautyPath>/<BeautyFile>', type='string')

if cmds.frameLayout('rsLayout_AovAOVsFrame', exists=1):
    mel.eval('redshiftUpdateActiveAovList')


# setAttr "rsAov_PuzzleMatte.redId" 6;

# Create material ids
material_ids = []
