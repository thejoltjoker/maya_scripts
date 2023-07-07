#!/usr/bin/env python3
"""meerkat.py
Description of meerkat.py.
"""
import os
import random
import re
from maya import cmds, mel
import logging

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

ATTRIBUTES = {'affectAlpha': 'affects_alpha',
              'affectShadows': 'affects_alpha',
              'anisotropy': 'anisotropy_orientation',
              'anisotropyAxis': 'anisotropy_orientation',
              'anisotropyDerivation': 'anisotropy_orientation',
              'anisotropyRotation': 'anisotropy_orientation',
              'attributeAliasList': 'coat_reflectivity',
              'binMembership': 'binMembership',
              'brdfType': 'refl_brdf',
              'bumpDeltaScale': 'ms_radius_scale',
              'bumpMap': 'bump_input',
              'bumpMapB': 'bump_inputB',
              'bumpMapG': 'bump_inputG',
              'bumpMapR': 'bump_inputR',
              'bumpMapType': 'outApiType',
              'bumpMult': 'bump_input',
              'bumpShadows': 'ms_radius0',
              'caching': 'caching',
              'color': 'outColor',
              'compensateExposure': 'coat_bump_inputR',
              'cutoffThreshold': 'coat_fresnel_mode',
              'diffuseColorAmount': 'diffuse_weight',
              'diffuseColorB': 'diffuse_colorB',
              'diffuseColorG': 'diffuse_colorG',
              'diffuseColorR': 'diffuse_colorR',
              'doubleSided': 'depth_override',
              'fixDarkEdges': 'refl_indirect',
              'fogBias': 'refl_roughness',
              'fogColor': 'outColor',
              'fogColorB': 'outColorB',
              'fogColorG': 'outColorG',
              'fogColorR': 'outColorR',
              'fogMult': 'outColor',
              'fresnelIOR': 'refl_ior',
              'frozen': 'frozen',
              'ggxOldTailFalloff': 'outApiClassification',
              'ggxTailFalloff': 'outApiClassification',
              'glossyFresnel': 'refl_fresnel_mode',
              'hilightGlossiness': 'refl_isGlossiness',
              'hilightGlossinessLock': 'refl_isGlossiness',
              'illumColor': 'outColor',
              'illumColorB': 'outColorB',
              'illumColorG': 'outColorG',
              'illumColorR': 'outColorR',
              'illumGI': 'block_volumes',
              'isHistoricallyInteresting': 'isHistoricallyInteresting',
              'lockFresnelIORToRefractionIOR': 'refl_aniso_rotation',
              'metalness': 'refl_metalness',
              'nodeState': 'nodeState',
              'opacityMap': 'opacity_color',
              'opacityMapB': 'opacity_colorB',
              'opacityMapG': 'opacity_colorG',
              'opacityMapR': 'opacity_color',
              'opacityMode': 'opacity_color',
              'outApiClassification': 'outApiClassification',
              'outApiType': 'outApiType',
              'outColor': 'outColor',
              'outColorB': 'outColorB',
              'outColorG': 'outColorG',
              'outColorR': 'outColorR',
              'outTransparency': 'coat_transmittance',
              'outTransparencyB': 'coat_transmittanceB',
              'outTransparencyG': 'coat_transmittanceG',
              'outTransparencyR': 'coat_transmittanceR',
              'reflInterpolation': 'refl_aniso_rotation',
              'reflMapColorThreshold': 'refl_colorR',
              'reflMapMaxRate': 'refl_samples',
              'reflMapMinRate': 'refl_indirect',
              'reflMapNormalThreshold': 'refl_aniso_rotation',
              'reflMapSamples': 'refl_samples',
              'reflectOnBackSide': 'refl_endmode',
              'reflectionAffectAlpha': 'affects_alpha',
              'reflectionColor': 'refl_color',
              'reflectionColorAmount': 'refl_weight',
              'reflectionColorB': 'refl_colorB',
              'reflectionColorG': 'refl_colorG',
              'reflectionColorR': 'refl_colorR',
              'reflectionDimDistance': 'refr_transmittance',
              'reflectionDimDistanceOn': 'refr_transmittance',
              'reflectionDimFallOff': 'refl_enablecutoff',
              'reflectionExitColor': 'refl_color',
              'reflectionExitColorB': 'refl_colorB',
              'reflectionExitColorG': 'refl_colorG',
              'reflectionExitColorR': 'refl_colorR',
              'reflectionGlossiness': 'refl_isGlossiness',
              'reflectionSubdivs': 'refl_metalness',
              'reflectionsMaxDepth': 'refl_depth',
              'refrDispersionAbbe': 'refr_abbe',
              'refrDispersionOn': 'refr_samples',
              'refrInterpolation': 'refl_aniso_rotation',
              'refrMapColorThreshold': 'refr_colorR',
              'refrMapMaxRate': 'refr_samples',
              'refrMapMinRate': 'refr_absorption_scale',
              'refrMapNormalThreshold': 'refr_samples',
              'refrMapSamples': 'refr_samples',
              'refractionColor': 'refr_color',
              'refractionColorAmount': 'refr_weight',
              'refractionColorB': 'refr_colorB',
              'refractionColorG': 'refr_colorG',
              'refractionColorR': 'refr_colorR',
              'refractionExitColor': 'refr_color',
              'refractionExitColorB': 'refr_colorB',
              'refractionExitColorG': 'refr_colorG',
              'refractionExitColorOn': 'refr_color',
              'refractionExitColorR': 'refr_colorR',
              'refractionGlossiness': 'refr_isGlossiness',
              'refractionIOR': 'refr_color',
              'refractionSubdivs': 'refr_absorption_scale',
              'refractionsMaxDepth': 'refr_depth',
              'roughnessAmount': 'refl_roughness',
              'scatterCoeff': 'ss_scatter_coeff',
              'scatterDir': 'ss_scatter_coeffR',
              'scatterLevels': 'ss_scatter_coeff',
              'scatterSubdivs': 'ss_scatter_coeffB',
              'softenEdge': 'coat_fresnel_mode',
              'sssEnvironment': 'sheen_direct',
              'sssOn': 'ss_amount',
              'swatchAlwaysRender': 'isHistoricallyInteresting',
              'swatchAutoUpdate': 'shaderNodeTemplate',
              'swatchExplicitUpdate': 'shaderNodeTemplate',
              'swatchMaxRes': 'ss_samples',
              'thickness': 'coat_thickness',
              'traceReflections': 'refl_reflectivity',
              'traceRefractions': 'refr_absorption_scale',
              'translucencyColor': 'transl_color',
              'translucencyColorB': 'transl_colorB',
              'translucencyColorG': 'transl_colorG',
              'translucencyColorR': 'transl_colorR',
              'useFresnel': 'refl_fresnel_mode',
              'useIrradianceMap': 'refr_transmittance',
              'useRoughness': 'diffuse_roughness'}


def remove_suffix(input_string):
    """Remove a suffix from a string

    Args:
        input_string:

    Returns:
        Everything before first underscore
    """
    result = re.findall(r'([^\s]+)_\w*$', input_string)
    if result:
        return result[0]
    return input_string


def create_redshift_materials():
    """Create redshift materials for all shading groups in scene

    Returns:
        list: material names
    """
    nodes = cmds.ls(type='shadingEngine')
    # setAttr "Standard_ncl1_27.color" -type double3 0.929032 0.684934 0.00364326 ;
    materials = []

    # Remove default shading groups from list
    for n in ['initialParticleSE', 'initialShadingGroup']:
        if n in nodes:
            nodes.pop(nodes.index(n))

    for sg in nodes:
        # Get material name
        material_name = remove_suffix(sg)

        # Create redshift material
        redshift_mtl = cmds.shadingNode('RedshiftMaterial', name='{}_shd'.format(material_name), asShader=True)
        # Create variables
        color, texture = None, None

        # Get the surface shader of the shading group
        sg_surface_shaders = shading_group_surface_shaders(sg)
        logger.info(sg_surface_shaders)
        if sg_surface_shaders:
            sg_surface_shader = sg_surface_shaders[0]

            vray_mtl = None

            if cmds.nodeType(sg_surface_shader) == 'VRayMeshMaterial':
                # Get input shader of mesh material
                shaders = cmds.listConnections('{}.shaders'.format(sg_surface_shader))
                if shaders:
                    vray_mtl = shaders[0]
            elif cmds.nodeType(sg_surface_shader) == 'VRayMtl':
                vray_mtl = sg_surface_shader

            if vray_mtl:
                color, texture = diffuse_from_vray_mtl(vray_mtl)

        else:
            color = color_from_shading_group(sg)

        logger.info(vray_mtl)

        # Set diffuse color of redshift material
        if color:
            color = color[0]
            cmds.setAttr('{}.diffuse_color'.format(redshift_mtl), *color, type="double3")
            logger.info('Set diffuse color to {}'.format(color))

        # Connect texture to redshift material
        if texture:
            texture = texture[0]
            cmds.connectAttr('{}.outColor'.format(texture), '{}.diffuse_color'.format(redshift_mtl))
            logger.info('Set texture to {}'.format(texture))

        # Set material values
        if vray_mtl:
            for vray_attr, rs_attr in ATTRIBUTES.items():
                try:
                    cmds.setAttr('{}.{}'.format(redshift_mtl, rs_attr),
                                 cmds.getAttr('{}.{}'.format(vray_mtl, vray_attr)))
                except:
                    continue
                    # cmds.warning(e)
        # Connect material to shading group
        cmds.connectAttr('{}.outColor'.format(redshift_mtl), '{}.surfaceShader'.format(sg), f=True)

        materials.append((redshift_mtl, sg))
        logger.info('---')

    return materials


def shading_group_surface_shaders(shading_group):
    """Return all connected surface shaders

    Args:
        shading_group: shading group node

    Returns:
        list: list of connected nodes
    """
    return cmds.listConnections('{}.surfaceShader'.format(shading_group), d=False, s=True)


def color_from_shading_group(shading_group):
    """Get the diffuse color from the connected material of a shading group

    Args:
        shading_group: shading group node

    Returns:
        tuple: double3 data for setAttr
    """
    color = None
    material = cmds.listConnections('{}.surfaceShader'.format(shading_group), d=False, s=True)

    if material:
        material = material[0]
        if cmds.attributeQuery('color', node=material, ex=True):
            color = cmds.getAttr('{}.color'.format(material))
        elif cmds.attributeQuery('diffuse_color', node=material, ex=True):
            color = cmds.getAttr('{}.diffuse_color'.format(material))
    if color:
        return color[0]
    return [0.5, 0.5, 0.5]


def diffuse_texture_from_shading_group(shading_group):
    """Get the diffuse texture from the connected material of a shading group

    Args:
        shading_group: shading group node

    Returns:
        str: attribute of texture output
    """
    color = None
    material = cmds.listConnections('{}.surfaceShader'.format(shading_group), d=False, s=True)

    if material:
        material = material[0]
        if cmds.attributeQuery('color', node=material, ex=True):
            color = cmds.getAttr('{}.color'.format(material))
            texture_out = cmds.listConnections('{}.color'.format(material), s=True, p=True)
            return texture_out

    return None


def diffuse_from_vray_mtl(vray_mtl):
    color = cmds.getAttr('{}.color'.format(vray_mtl))
    texture = cmds.listConnections('{}.color'.format(vray_mtl), s=True)
    return color, texture


def search_and_replace_filenames(node, search_for, replace_with, attribute="fileTextureName", attribute_type='string'):
    search_for = search_for.replace('\\', '/')
    replace_with = replace_with.replace('\\', '/')

    # Example: Print the file path
    file_path = cmds.getAttr(node + '.' + attribute).replace('\\', '/')
    new_file_path = file_path.replace(search_for, replace_with)
    cmds.setAttr(node + '.' + attribute, new_file_path, type=attribute_type)
    return node


import maya.cmds as cmds
import maya.cmds as cmds


def get_connected_anim_curves(node):
    anim_curves = []

    # Get all connections of the specified node
    connections = cmds.listConnections(node, destination=False)

    if not connections:
        print("No connections found for node:", node)
        return anim_curves

    # Filter the connections to find animCurve nodes
    for connection in connections:
        # Check if the connection is an animCurve node
        if "animCurve" in cmds.nodeType(connection):
            anim_curves.append(connection)

    return anim_curves


def offset_keyframes(node, offset):
    connected_anim_curves = get_connected_anim_curves(node)

    if connected_anim_curves:
        for anim_curve in connected_anim_curves:
            cmds.select(anim_curve)
            logger.info('Offsetting keyframes by {offset} frames on {node}'.format(offset=offset, node=anim_curve))
            cmds.keyframe(edit=True, relative=True, option="over", timeChange=offset)
    cmds.select()


def main_standalone():
    import maya.standalone
    maya.standalone.initialize()
    cmds.loadPlugin('redshift4maya.mll')

    # Import scene
    cmds.file(r'L:\assets\stadium\references\Stadium_LM_MAYA\Stadium_LM_Daylight.mb', i=True)

    # Do things
    create_redshift_materials()

    mel.eval('MLdeleteUnused;')

    # Save file
    cmds.file(rename=r'L:\assets\stadium\sandbox\stadium_rs_v001.mb')
    cmds.file(save=True)
    maya.standalone.uninitialize()


def fix_chairs():
    import maya.standalone
    maya.standalone.initialize()
    cmds.loadPlugin('redshift4maya.mll')
    seats_path = r'L:\assets\stadium\references\Stadium_LM_MAYA\Stadium_Seats'
    for f in os.listdir(seats_path):
        scene_path = os.path.join(seats_path, f)
        logger.info(scene_path)
        # Import scene
        cmds.file(scene_path, i=True)

    # Do things
    create_redshift_materials()

    mel.eval('MLdeleteUnused;')

    # Save file
    cmds.file(rename=r'L:\assets\stadium\sandbox\stadium_chairs_rs_v001.mb')
    cmds.file(save=True)
    maya.standalone.uninitialize()


def prep_fans():
    import maya.standalone
    maya.standalone.initialize()

    # Set the frame rate to 25 fps
    cmds.currentUnit(time='pal')
    cmds.playbackOptions(ps=25, minTime=1, maxTime=100)
    cmds.currentTime(1)

    cmds.loadPlugin('redshift4maya.mll')
    fans_path = r'L:\assets\stadium\references\Stadium_LM_MAYA\Characters_Fans'
    for f in os.listdir(fans_path):
        scene_path = os.path.join(fans_path, f)
        offset_value = random.randint(0, 25)

        logger.info(scene_path)
        # Import scene
        logger.info('Importing {}'.format(f))
        """file -import -type "mayaBinary" -gr  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "Fan_F_02" -options "v=0;p=17;f=0"  -pr  -importTimeRange "combine" "//10.21.110.10/libraries/assets/stadium/references/Stadium_LM_MAYA/Characters_Fans/Fan_F_02.mb";"""
        namespace = os.path.splitext(f)[0]
        cmds.file(scene_path, i=True, gr=True, namespace=namespace)

        # Remove inherit transform on mesh
        """setAttr "Fan_F_01:Fan_F_01_Mesh.inheritsTransform" 0;"""
        if not any(x in namespace for x in ['Flag', 'Scarf']):
            cmds.setAttr('{namespace}:{namespace}_Mesh.inheritsTransform'.format(namespace=namespace), 0)

        # for node in cmds.ls(sl=True):
        # group_name = cmds.listRelatives('group', children=True)[0].split(':')[-1].encode('utf-8') + '_grp'
        group_name = namespace + '_grp'
        group = cmds.rename('group', group_name)
        cmds.xform(group_name, piv=(0, 0, 0), worldSpace=True)

        # Loop animation
        skeleton = namespace + ':Biped'

        for joint in cmds.listRelatives(group, allDescendents=True, type='joint'):
            # Offset keyframes
            offset_keyframes(joint, offset_value)

            # Loop animation
            cmds.setInfinity(joint, pri='cycle', poi='cycle')

        # offset_keyframes(skeleton, offset_value)
        # cmds.setInfinity(skeleton, pri='cycle', poi='cycle')

    # Do things
    create_redshift_materials()
    # Get a list of all file nodes in the scene
    file_nodes = cmds.ls(type='file')
    for fn in file_nodes:
        search_and_replace_filenames(fn, 'E:\\PROJEKTY MAX\\!!!_CHARACTERS_MAYA\\\\',
                                     'L:\\assets\\stadium\\references\\Stadium_LM_MAYA\\')
    # Replace cache paths
    cache_nodes = cmds.ls(type='cacheFile')
    for cn in cache_nodes:
        name = cmds.getAttr(cn + '.cacheName')
        search_and_replace_filenames(cn, 'L:\\assets\\stadium\\references\\Stadium_LM_MAYA\\Characters_Fans\\',
                                     'L:\\assets\\stadium\\references\\Stadium_LM_MAYA\\cache\\nCache\\{}'.format(name),
                                     attribute='cachePath',
                                     attribute_type='string')

    mel.eval('MLdeleteUnused;')

    # Save file
    cmds.file(rename=r'L:\assets\stadium\sandbox\stadium_fans_rs_v001.mb')
    cmds.file(save=True)
    maya.standalone.uninitialize()


def main():
    """docstring for main"""
    create_redshift_materials()


if __name__ == '__main__':
    # main_standalone()
    # fix_chairs()
    prep_fans()
