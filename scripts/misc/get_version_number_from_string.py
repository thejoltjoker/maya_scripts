#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
get_version_number_from_string.py
Description of get_version_number_from_string.py.
"""

import os
import re


def extract_versions():
    """docstring for main"""
    full_path = r'E:/Dropbox_bak/projects/2018/0100_seq_am/3d/assets/chars/butterfly/rig/publish/am_butterfly_rig_v037.ma'
    filename, ext = os.path.splitext(os.path.basename(full_path))
    versions = [p for p in filename.split('_') if re.match(r"v\d+", p)]
    version_numbers = []
    for ver in versions:
        version_numbers.append(int(ver[1:]))

    print(version_numbers)


if __name__ == '__main__':
    extract_versions()
