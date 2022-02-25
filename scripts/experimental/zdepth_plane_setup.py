import maya.cmds as cmds

# 1. Determine which camera is being rendered
allCameras = cmds.ls( cameras=True )
for camera in allCameras:
	#print cams
	if cmds.getAttr(camera+'.renderable') == True:
		renderCam = camera

#print renderCam
# 2. Use the camera position and loop through objects to see which object is furthest away

#cameraPosition = cmds.getAttr(renderCam+'.translate')
allObjects = cmds.ls( type='mesh' )
for obj in allObjects:
	#if cmds.nodeType(obj) == 'mesh':
	
	print cmds.listRelatives(obj, parent=True)

#for obj in allObjects:
#	print cmds.getAttr(obj+'.translate')

# 3. Create plane
# 4. Place it 5% behind the object furthest from camera
# 5. Turn off visibility
