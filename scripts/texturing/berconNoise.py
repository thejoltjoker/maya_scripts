import maya.cmds as cmds

# Create fractal node
myFractal = cmds.shadingNode('fractal', asShader=True)
myFractalPlacement = cmds.shadingNode('place2dTexture', asUtility=True)

## Connect placement node
cmds.connectAttr(myFractalPlacement+'.outUV', myFractal+'.uv')
cmds.connectAttr(myFractalPlacement+'.outUvFilterSize', myFractal+'.uvFilterSize')


# Create noise node
myNoise = cmds.shadingNode('noise', asShader=True)
myNoisePlacement = cmds.shadingNode('place2dTexture', asUtility=True)

## Connect to placement node
cmds.connectAttr(myNoisePlacement+'.outUV', myNoise+'.uv')
cmds.connectAttr(myNoisePlacement+'.outUvFilterSize', myNoise+'.uvFilterSize')


# Connect noise nodes
cmds.connectAttr(myFractal+'.outColorR', myNoisePlacement+'.offsetU')
cmds.connectAttr(myFractal+'.outColorR', myNoisePlacement+'.offsetV')
