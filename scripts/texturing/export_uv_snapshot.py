#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
export_uv_snapshot.py
Description of export_uv_snapshot.py.
"""
import os
import maya.cmds as cmds
import string


def convert_filename(file):
    valid_chars = " -_.{letters}{digits}".format(
        letters=string.ascii_letters, digits=string.digits)
    filename = ''.join(c for c in file if c in valid_chars)
    filename = filename.replace(' ', '_')
    return filename


def main():
    """docstring for main"""
    sel = cmds.ls(sl=True)[0]
    scene_path = cmds.file(sn=True, q=True)
    scene_name = os.path.basename(scene_path)
    export_path = os.path.join(
        os.path.dirname(scene_path),
        '..',
        '..',
        'exports')
    out_filename = '_'.join(
        [os.path.splitext(scene_name)[0], convert_filename(sel), 'uv.png'])
    out_file = os.path.abspath(os.path.join(export_path, out_filename))

    if not os.path.exists(export_path):
        os.makedirs(export_path)
    cmds.uvSnapshot(aa=True, n=out_file, xr=4096, yr=4096,
                    r=255, g=255, b=255, o=True, ff='png')


if __name__ == '__main__':
    main()
