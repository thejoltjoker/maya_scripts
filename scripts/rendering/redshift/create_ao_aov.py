#!/usr/bin/env python3
"""create_ao_aov.py
Description of create_ao_aov.py.
"""
# shadingNode -asUtility RedshiftAmbientOcclusion;
# // Result: rsAmbientOcclusion2 //
# defaultNavigation -connectToExisting -destination rsAov_Custom.defaultShader -source rsAmbientOcclusion2; window -e -vis false createRenderNodeWindow;
# connectAttr -force rsAmbientOcclusion2.outColor rsAov_Custom.defaultShader;
# // Result: Connected rsAmbientOcclusion2.outColor to rsAov_Custom.defaultShader. //
# // Result: createRenderNodeWindow //
from maya import cmds, mel


def main():
    """Create a custom aov with an ambient occlusion shader.
    """
    # Create custom aov
    aov_node = cmds.rsCreateAov(type='Custom', name='AmbientOcclusion')
    cmds.setAttr(aov_node + '.name', 'AmbientOcclusion', type='string')

    # Update aov list
    mel.eval('redshiftUpdateActiveAovList()')

    # Create ambient occlusion material
    material = cmds.shadingNode('RedshiftAmbientOcclusion', name='ambientOcclusion_shd', asUtility=True)

    # Connect material to aov
    cmds.connectAttr('{}.outColor'.format(material), '{}.defaultShader'.format(aov_node), f=True)

    return aov_node


if __name__ == '__main__':
    main()
