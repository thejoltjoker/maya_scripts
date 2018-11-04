#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
enable_override_aovs.py
Description of enable_override_aovs.py.
"""


def main():
    """docstring for main"""
    aovs = cmds.ls(type='RedshiftAOV')
    for aov in aovs:
        cmds.editRenderLayerAdjustment("{}.enabled".format(aov))
        print("Enabled override for aov: {}".format(aov))


if __name__ == '__main__':
    main()
