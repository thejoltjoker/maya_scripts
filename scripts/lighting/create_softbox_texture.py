"""create_softbox_texture.py
Description of create_softbox_texture.py.
"""
from maya import cmds


def main():
    """docstring for main"""
    # // Info:  [Redshift] Stopping IPR //
    # shadingNode -asTexture ramp;
    cmds.shadingNode('ramp', asTexture=True)
    # // Result: ramp2 //
    # shadingNode -asUtility place2dTexture;

    cmds.shadingNode('place2dTexture', asUtility=True)

    # // Result: place2dTexture4 //
    # connectAttr place2dTexture4.outUV ramp2.uv;
    # // Result: Connected place2dTexture4.outUV to ramp2.uvCoord. //
    # connectAttr place2dTexture4.outUvFilterSize ramp2.uvFilterSize;
    # // Result: Connected place2dTexture4.outUvFilterSize to ramp2.uvFilterSize. //
    # defaultNavigation -force true -connectToExisting -source ramp2 -destination |lights_A_grp|rimLightOffset_grp1|rimLight_lgt|rimLight_lgtShape.color; window -e -vis false createRenderNodeWindow;
    # // Error: file: //10.21.110.11/pipeline/Redshift/Plugins/Maya/Common/scripts/override/2022/connectNodeToAttrOverride.mel line 85: More than one object matches name: rimLight_lgtShape //
    # connectAttr -force ramp2.outColor rimLightOffset_grp1|rimLight_lgt|rimLight_lgtShape.color;
    # // Result: Connected ramp2.outColor to rimLight_lgtShape.color. //
    # // Result: createRenderNodeWindow //
    # setAttr "ramp2.type" 5;
    # setAttr "ramp2.interpolation" 2;
    # setAttr "ramp2.colorEntryList[0].position" 0.855491;
    # setAttr "ramp2.colorEntryList[1].position" 0;
    # setAttr "ramp2.colorEntryList[0].position" 1;
    pass

if __name__ == '__main__':
    main()