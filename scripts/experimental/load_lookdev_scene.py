#!/usr/bin/env python
"""
load_lookdev_scene.py
Description of load_lookdev_scene.py.
"""
import os
import logging
logger = logging.getLogger(__name__)

import maya.cmds as cmds


def main():
    """docstring for main"""
    template_folder_path = r'//SEQ-LIVE/live_projects/People/Johannes/lookdev/scenes'

    logger.info("Checking " + template_folder_path +
                " for the latest published template")

    template_files = []
    for filename in os.listdir(template_folder_path):
        if filename.endswith('.ma'):
            template_files.append("/".join([template_folder_path, filename]))

    template_files.sort(reverse=True)

    template = template_files[0]

    logger.info("Maya: Template to use is " + template)

    cmds.file(template, reference=True, namespace='lookdev_set')


if __name__ == '__main__':
    main()