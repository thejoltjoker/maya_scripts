import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.cmds as cmds

rs = renderSetup.instance()

# Get selected objects
camera = cmds.ls(selection=True)[0]
layerName = camera.split(':')[1].replace('_cam', '')
camShape = cmds.listRelatives(camera, shapes=True)[0]

# Get frame range
frames = cmds.getAttr(camShape + '.notes').split('-')
startFrame = frames[0].rstrip()
endFrame = frames[-1].rstrip()

# Create and append the render layer
try:
    rl = rs.getRenderLayer(layerName)
except Exception as e:
    rl = rs.createRenderLayer(layerName)

# Set renderable camera
print("Setting camera settings on " + camShape)
cameras = cmds.ls(cameras=True)
camCol = rl.createCollection('cam_' + layerName)
camSel = camCol.getSelector()
camSel.setPattern(camera)
camSSel = camSel.staticSelection
camSSel.add(camera)
camSSel.add(camShape)
for cam in cameras:
    try:
        camCol.createAbsoluteOverride(cam, 'renderable')
        if camShape in cam:
            cmds.setAttr(cam + '.renderable', 1)
        else:
            cmds.setAttr(cam + '.renderable', 0)

    except:
        print(cam)

# Create and append 2 collections
include = rl.createCollection("include")
include.getSelector().setPattern('*')

# Create exclude collection
exclude = rl.createCollection("exclude")
exclude.setSelfEnabled(False)

# Switch to new layer
rs.switchToLayer(rl)

# Frame range
rsInstance = rl.renderSettingsCollectionInstance()
rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'startFrame')
rsInstance.createAbsoluteOverride('defaultRenderGlobals', 'endFrame')

cmds.setAttr('defaultRenderGlobals.startFrame', startFrame)
cmds.setAttr('defaultRenderGlobals.endFrame', endFrame)

current_layer = cmds.editRenderLayerGlobals(query=True, currentRenderLayer=True)
for cam in cmds.ls(cameras=True):
    cmds.editRenderLayerAdjustment(cam + '.primaryEngine')
    cmds.setAttr(cam + '.primaryEngine', 0)
