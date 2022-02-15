# check if already baked stuff
# there are existing baked nodes, create new or export.

import maya.cmds as cmds
import sys
import os
import maya.mel as mel

# find out which system the code is running on
from sys import platform as systemOS

if systemOS == "linux" or systemOS == "linux2":
     print("Unable to set server path")
elif systemOS == "darwin":
     mayaScriptPath = '/Volumes/assets/Python'
elif systemOS == "win32":
     mayaScriptPath = 'A:/Scripts/Python'

# set units to foot
cmds.currentUnit( linear='foot' )
print("Units set to foot.")

# source AE export
mel.eval('source "%s/sequence/maya/tools/rcExport2AE/rcExport2AE_launch.mel"' % mayaScriptPath)

# select all locators
cmds.select(d=True)
selNodes = "_LOC"
allObjs = cmds.ls()

for obj in allObjs:
    if obj.endswith(selNodes):
        cmds.select(obj, add=True)

print("Locators selected.")

# select renderable cameras
allCams = cmds.ls(ca=True)
for cam in allCams:
    camRend = cmds.getAttr(cam+".renderable")
    if camRend:
        camTransform = cmds.listRelatives(cam, parent=True)
        cmds.select(camTransform, add=True)

# bake selected nodes
mel.eval('btnCmdBake()')

# select baked nodes
cmds.select(d=True)

selNodes = "_baked"

for obj in allObjs:
    if obj.endswith(selNodes):
        cmds.select(obj, add=True)

print("Baked nodes selected.")

multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
filename = cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2)
cmds.file( filename[0], type='mayaAscii', exportSelected=True )
cmds.warning('Nodes exported.')