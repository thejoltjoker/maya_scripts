#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create_udim_mask.py
Description of create_udim_mask.py.
"""


def main():
    """docstring for main"""
    pass


if __name__ == '__main__':
    main()
# shadingNode -asTexture ramp;
# // ramp1 //
# shadingNode -asUtility place2dTexture;
# // place2dTexture37 //
# connectAttr place2dTexture37.outUV ramp1.uv;
# // Connected place2dTexture37.outUV to ramp1.uvCoord. //
# connectAttr place2dTexture37.outUvFilterSize ramp1.uvFilterSize;
# // Connected place2dTexture37.outUvFilterSize to ramp1.uvFilterSize. //
# removeMultiInstance -break true ramp1.colorEntryList[0];
# setAttr "ramp1.defaultColor" -type double3 0 0 0 ;.
# setAttr "place2dTexture37.wrapU" 0;
# setAttr "place2dTexture37.wrapV" 0;