import maya.standalone

print "imported maya.standalone"

maya.standalone.initialize(name='python')
print "Maya Standalone Initialized"

# DO MAYA STUFF HERE
import maya.cmds as cmds

cmds.polySphere(n="extraClass")

if cmds.getAttr('defaultRenderGlobals.currentRenderer') != 'redshift':
    cmds.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')

mel.eval('redshiftGetRedshiftOptionsNode(true)')

# File settings
cmds.setAttr('redshiftOptions.imageFormat', 1)
cmds.setAttr('redshiftOptions.noSaveImage', 1)
cmds.setAttr('redshiftOptions.exrForceMultilayer', 1)
cmds.setAttr('defaultRenderGlobals.ifp', '<Scene>/<Scene>_<RenderLayer>/<Scene>_<RenderLayer>', type='string')
# Animation settings
maxFrame = cmds.playbackOptions(q=True, max=True)
minFrame = cmds.playbackOptions(q=True, min=True)
cmds.setAttr('defaultRenderGlobals.animation', 1)
# cmds.setAttr('defaultRenderGlobals.startFrame', minFrame)
# cmds.setAttr('defaultRenderGlobals.endFrame', maxFrame)
cmds.setAttr('defaultRenderGlobals.byFrameStep', 1)
cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)

# Output settings
cmds.setAttr('defaultResolution.width', 1920)
cmds.setAttr('defaultResolution.height', 1080)
cmds.setAttr('defaultResolution.pixelAspect', 1)

# Sampler settings
cmds.setAttr('redshiftOptions.autoProgressiveRenderingIprEnabled', 1)
cmds.setAttr('redshiftOptions.unifiedRandomizePattern', 1)

# Motion blur settings
cmds.setAttr('redshiftOptions.motionBlurEnable', 1)
cmds.setAttr('redshiftOptions.motionBlurFrameDuration', 0.5)
cmds.setAttr('redshiftOptions.motionBlurShutterStart', 0.25)
cmds.setAttr('redshiftOptions.motionBlurShutterEnd', 0.75)
cmds.setAttr('redshiftOptions.motionBlurShutterEfficiency', 0.5)
cmds.setAttr('redshiftOptions.motionBlurDeformationEnable', 1)

cmds.file( rename=r'C:\mayapyTest\submission.ma' )
cmds.file( save=True, type='mayaAscii', f=True )
print "File Saved"

maya.standalone.uninitialize()

exit()