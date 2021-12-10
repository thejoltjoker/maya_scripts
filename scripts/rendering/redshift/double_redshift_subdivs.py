#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
double_redshift_subdivs.py

Double the samples in render settings
"""
import maya.cmds as cmds


def main():
    """docstring for main"""

    min_samples = 4
    old_max_samples = cmds.getAttr("redshiftOptions.unifiedMaxSamples")
    max_samples = old_max_samples * 2

    cmds.setAttr("redshiftOptions.unifiedMinSamples", min_samples)
    cmds.setAttr("redshiftOptions.unifiedMaxSamples", max_samples)

    cmds.setAttr("redshiftOptions.reflectionSamplesOverrideReplace",
                 max_samples * 2)
    cmds.setAttr("redshiftOptions.refractionSamplesOverrideReplace",
                 max_samples * 2)
    cmds.setAttr("redshiftOptions.AOSamplesOverrideReplace", max_samples * 2)
    cmds.setAttr("redshiftOptions.lightSamplesOverrideReplace", max_samples * 2)
    cmds.setAttr("redshiftOptions.volumeSamplesOverrideReplace", max_samples * 2)
    cmds.setAttr(
        "redshiftOptions.singleScatteringSamplesOverrideReplace", max_samples * 2)
    cmds.setAttr("redshiftOptions.bruteForceGINumRays", max_samples * 2)


if __name__ == '__main__':
    main()
