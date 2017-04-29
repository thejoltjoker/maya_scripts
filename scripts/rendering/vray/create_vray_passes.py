"""
create_vray_passes.py

Create vray render elements.
"""
import maya.cmds as cmds
import maya.mel as mel

def createBeautyPasses():
    # Create diffuse channel
    passToMake = 'vrayRE_Diffuse'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement diffuseChannel;')

    # Create reflect channel
    passToMake = 'vrayRE_Reflection'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement reflectChannel;')

    # Create refract channel
    passToMake = 'vrayRE_Refraction'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement refractChannel;')

    # Create specular channel
    passToMake = 'vrayRE_Specular'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement specularChannel;')

    # Create lighting channel
    passToMake = 'vrayRE_Lighting'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement lightingChannel;')

    # Create GI channel
    passToMake = 'vrayRE_GI'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement giChannel;')

    # Create rawGI channel
    passToMake = 'vrayRE_Raw_GI'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement rawGiChannel;')

    # Create selfIllum channel
    passToMake = 'vrayRE_Self_Illumination'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement selfIllumChannel;')

    cmds.warning('Beauty passes created.')

# vrayAddRenderElement bumpNormalsChannel;
# vrayAddRenderElement ExtraTexElement;
# vrayAddRenderElement zdepthChannel;
def createUtilityPasses():
    # Create samplerInfo node
    samplerNodeName = 'rendering_samplerInfo'
    if not cmds.objExists(samplerNodeName):
        samplerNode = cmds.shadingNode('samplerInfo', asUtility=True)
        samplerNode = cmds.rename(samplerNode, samplerNodeName)

    # Create GI channel
    passToMake = 'vrayRE_GI'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement giChannel;')

    # Create rawGI channel
    passToMake = 'vrayRE_Raw_GI'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement rawGiChannel;')

    # Create selfIllum channel
    passToMake = 'vrayRE_Self_Illumination'
    if not cmds.objExists(passToMake):
        renderElement = mel.eval('vrayAddRenderElement selfIllumChannel;')

    layerToMake = 'zDepth'
    if not cmds.objExists(layerToMake):
        renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
        renderElement = cmds.rename(renderElement, layerToMake)
        cmds.setAttr(layerToMake + '.vray_name_zdepth', layerToMake, type = 'string')
        cmds.setAttr(layerToMake + '.vray_depthFromCamera_zdepth', True)
        cmds.setAttr(layerToMake + '.vray_depthClamp', False)
        cmds.setAttr(layerToMake + '.vray_filtering_zdepth', False)
    # zDepth with AA
    layerToMake = 'zDepthAA'
    if not cmds.objExists(layerToMake):
        renderElement = mel.eval('vrayAddRenderElement zdepthChannel;')
        renderElement = cmds.rename(renderElement, layerToMake)
        cmds.setAttr(layerToMake + '.vray_name_zdepth', layerToMake , type = 'string')
        cmds.setAttr(layerToMake + '.vray_depthFromCamera_zdepth', True)
        cmds.setAttr(layerToMake + '.vray_depthClamp', False)
        cmds.setAttr(layerToMake + '.vray_filtering_zdepth', True)
    # UVs
    layerToMake = 'UV'
    if not cmds.objExists(layerToMake):
        renderElement = mel.eval('vrayAddRenderElement ExtraTexElement;')
        cmds.rename(renderElement,layerToMake)
        cmds.setAttr(layerToMake + '.vray_name_extratex', layerToMake, type = 'string')
        cmds.setAttr(layerToMake + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        cmds.connectAttr(samplerNodeName + '.uvCoord.uCoord', layerToMake + '.vray_texture_extratex.vray_texture_extratexR')
        cmds.connectAttr(samplerNodeName + '.uvCoord.vCoord', layerToMake + '.vray_texture_extratex.vray_texture_extratexG')
        cmds.setAttr(layerToMake + '.vray_filtering_extratex', False)
    # worldXYZ
    layerToMake = 'worldXYZ'
    if not cmds.objExists(layerToMake):
        renderElement = mel.eval('vrayAddRenderElement ExtraTexElement;')
        cmds.rename(renderElement,layerToMake)
        cmds.setAttr(layerToMake + '.vray_name_extratex', layerToMake, type = 'string')
        cmds.setAttr(layerToMake + '.vray_explicit_name_extratex', 'worldXYZ', type = 'string')
        cmds.setAttr(layerToMake + '.vray_considerforaa_extratex', False)
        cmds.connectAttr(samplerNodeName + '.pointWorld', layerToMake+'.vray_texture_extratex')
    # Ambient Occlusion
    layerToMake = 'AO'
    nodeToMake = 'ao_tex'
    if not cmds.objExists(layerToMake):
        if not cmds.objExists(nodeToMake):
            newNode = cmds.shadingNode('VRayDirt', name = nodeToMake, asTexture=True)
            cmds.setAttr(newNode + '.invertNormal', False)
            cmds.setAttr(newNode + '.ignoreForGi', 0)
            cmds.setAttr(newNode + '.blackColor', -0.5, -0.5, -0.5, type='double3')
            cmds.setAttr(newNode + '.falloff', 5)
        renderElement = mel.eval('vrayAddRenderElement ExtraTexElement;')
        renderElement = cmds.rename(renderElement, layerToMake)
        cmds.setAttr(layerToMake + '.vray_name_extratex', layerToMake, type = 'string')
        cmds.setAttr(layerToMake + '.vray_explicit_name_extratex', layerToMake, type = 'string')
        cmds.connectAttr(nodeToMake + '.outColor', layerToMake + '.vray_texture_extratex')
    cmds.warning('Utility passes created.')