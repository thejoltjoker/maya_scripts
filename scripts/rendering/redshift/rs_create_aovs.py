"""
rs_create_aovs.py
"""
import maya.cmds as cmds
import maya.mel as mel

def testRenderer():
    if cmds.getAttr("defaultRenderGlobals.currentRenderer") != 'redshift':
        cmds.warning("Redshift is not current renderer")
        return False
    else:
        cmds.setAttr('redshiftOptions.imageFormat', 1)
        print "Image format set to exr."

def createRedshiftBeautyAovs():
    # Create beauty passes
    # These passes are chosen based on the AOV tutorial in the Redshift manual http://docs.redshift3d.com/Default.html#I/AOV Tutorial.html
    existing_aovs = cmds.ls(type='RedshiftAOV')
    existing_aovs_nice = []
    for aovNode in existing_aovs:
        aov_nice = cmds.getAttr(aovNode+'.aovType')
        existing_aovs_nice.append(aov_nice)

    beauty_aovs = [ 'Diffuse Filter',
                    'Diffuse Lighting Raw',
                    'Global Illumination Raw',
                    'Sub Surface Scatter',
                    'Specular Lighting',
                    'Reflections',
                    'Refractions',
                    'Emission',
                    'Caustics']

    for aov in beauty_aovs:
        if aov not in existing_aovs_nice:
            aovNode = cmds.rsCreateAov(type=aov)
            cmds.setAttr(aovNode+'.filePrefix', '<BeautyPath>/<BeautyFile>', type='string')
        else:
            print aov+" already exists and has been skipped."

    if cmds.frameLayout('rsLayout_AovAOVsFrame', exists=1):
        mel.eval('redshiftUpdateActiveAovList')

def createRedshiftUtilAovs():
    # Create utility passes
    # These passes are chosen based on my own needs.
    existing_aovs = cmds.ls(type='RedshiftAOV')
    existing_aovs_nice = []
    for aovNode in existing_aovs:
        aov_nice = cmds.getAttr(aovNode+'.aovType')
        existing_aovs_nice.append(aov_nice)

    util_aovs = [   'Bump Normals',
                    'Depth',
                    'Motion Vectors',
                    'Normals',
                    'World Position']

    for aov in util_aovs:
        if aov not in existing_aovs_nice:
            aovNode = cmds.rsCreateAov(type=aov)
            cmds.setAttr(aovNode+'.filePrefix', '<BeautyPath>/<BeautyFile>', type='string')
            if aov == 'Depth':
                cmds.setAttr(aovNode+'.normalizeZeroToOne', 1)
        else:
            print aov+" already exists and has been skipped."

    if cmds.frameLayout('rsLayout_AovAOVsFrame', exists=1):
        mel.eval('redshiftUpdateActiveAovList')

def createAovSwitch():
    pass_holder = cmds.polyCube(n='rsPassHolder')[0]
    cmds.setAttr(pass_holder+'.visibility', 0, k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.tx', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.ty', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.tz', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.rx', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.ry', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.rz', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.sx', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.sy', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder+'.sz', k=False, l=True, cb=False)
    cmds.delete(pass_holder, ch=True)

    # Create pass holder group
    pass_holder_grp = cmds.group(pass_holder, name='rsAOVControl')
    cmds.setAttr(pass_holder_grp+'.visibility', 1, k=False, cb=False)
    cmds.setAttr(pass_holder_grp+'.tx', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.ty', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.tz', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.rx', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.ry', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.rz', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.sx', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.sy', k=False, l=True, cb=False)
    cmds.setAttr(pass_holder_grp+'.sz', k=False, l=True, cb=False)
    cmds.delete(pass_holder_grp, ch=True)
    cmds.addAttr(pass_holder_grp, ln='enableBeauty', nn='Enable Beauty AOVs', at='bool', k=True)
    cmds.addAttr(pass_holder_grp, ln='enableUtility', nn='Enable Utility AOVs', at='bool', k=True)

    beauty_aovs = [ 'Diffuse Filter',
                    'Diffuse Lighting Raw',
                    'Global Illumination Raw',
                    'Sub Surface Scatter',
                    'Specular Lighting',
                    'Reflections',
                    'Refractions',
                    'Emission',
                    'Caustics']

    util_aovs = [   'Bump Normals',
                    'Depth',
                    'Motion Vectors',
                    'Normals',
                    'World Position']

    # Connect attributes
    existing_aovs = cmds.ls(type='RedshiftAOV')
    for aovNode in existing_aovs:
        aov_nice = cmds.getAttr(aovNode+'.aovType')
        if aov_nice in beauty_aovs:
            cmds.connectAttr(pass_holder_grp+'.enableBeauty', aovNode+'.enabled')
        elif aov_nice in util_aovs:
            cmds.connectAttr(pass_holder_grp+'.enableUtility', aovNode+'.enabled')
        else:
            print aov_nice+" was created manually and was not assigned to the AOV control."