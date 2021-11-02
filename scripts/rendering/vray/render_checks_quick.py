import maya.cmds as cmds

attrStartFrame = cmds.getAttr("defaultRenderGlobals.startFrame")
attrEndFrame = cmds.getAttr("defaultRenderGlobals.endFrame")

attrMinSubdivs = cmds.getAttr("vraySettings.dmcMinSubdivs")
attrMaxSubdivs = cmds.getAttr("vraySettings.dmcMaxSubdivs")
attrDmcThreshold = cmds.getAttr("vraySettings.dmcThreshold")

giStatus = cmds.getAttr("vraySettings.giOn")
mbStatus = cmds.getAttr("vraySettings.cam_mbOn")
dispStatus = cmds.getAttr("vraySettings.globopt_geom_displacement")

print ''
print ''
print ''
print ''
print ''
print '### RENDER CHECKS ###'


# print frame range
print 'frame range: '+str(attrStartFrame)+' - '+str(attrEndFrame)
print ''
# print rendercam
allCams = cmds.ls(ca=True)
for cam in allCams:
    camRend = cmds.getAttr(cam+".renderable")
    if camRend:
        print 'rendercam: '+str(cam)
print ''
# print resolution

# print subdivs
print 'Min sampler subdivs is set to '+str(attrMinSubdivs)
print 'Max sampler subdivs is set to '+str(attrMaxSubdivs)
print 'Sampler threshold is set to '+str(attrDmcThreshold)
print ''

# print gi status
if giStatus:
    print 'Global illumination is turned ON'
else:
    print 'Global illumination is turned OFF'
print ''
# print mb status
if mbStatus:
    print 'Motion blur is turned ON'
else:
    print 'Motion blur is turned OFF'
print ''
# print disp status
if mbStatus:
    print 'Displacement is turned ON'
else:
    print 'Displacement is turned OFF'
print ''
print '### DONE ###'