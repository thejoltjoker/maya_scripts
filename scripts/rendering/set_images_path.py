#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
set_images_path.py
Set image path to match the pipeline and create output folder if it doesn't exist.
"""
import maya.cmds as cmds
import os


def main():
    """docstring for main"""
    file_path = cmds.file(q=True, exn=True)
    file_directory = os.path.dirname(file_path)

    # Construct output path
    render_path = os.path.abspath(os.path.join(file_directory, '..', '..', '..', 'published', 'render'))

    # Check if parent folder exists
    if os.path.isdir(os.path.dirname(render_path)):

        # Create output folder so Deadline won't complain
        if not os.path.isdir(render_path):
            os.mkdir(render_path)

        # Set images in workspace
        cmds.workspace(fileRule=['images', render_path])

    # Print workspace
    rules = cmds.workspace(fileRule=True, q=True)
    img_index = rules.index("images") + 1
    cmds.warning('Images path is {0}'.format(rules[img_index]))


if __name__ == '__main__':
    main()
