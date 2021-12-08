#!/usr/bin/env python
"""
list_all_texture_files.py
Description of list_all_texture_files.py.
"""
import os
import maya.cmds as cmds
import subprocess
from pprint import pprint
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


def replace_path(node, path):
    cmds.setAttr("{}.fileTextureName".format(node), path, type='string')


def main():
    """docstring for main"""
    files = []
    nodes = cmds.ls(type='file', long=True)

    for node in nodes:
        path = cmds.getAttr(f'{node}.fileTextureName')
        if '$ACTIVE_LIBRARY_PATH' in path:
            path = path.split('$ACTIVE_LIBRARY_PATH')[-1]
            path = path.replace('$ACTIVE_LIBRARY_PATH', os.getenv('ACTIVE_LIBRARY_PATH'))
        path = os.path.abspath(path)
        replace_path(node, path)
        file = {
            'node': node,
            'path': path,
            'filename': os.path.basename(cmds.getAttr(f'{node}.fileTextureName')),
            'color_space': cmds.getAttr(f'{node}.colorSpace'),
            'descendants': cmds.listRelatives(node, ad=True),
            'connected_to': list(dict.fromkeys(cmds.listConnections(node))),
            'parents': cmds.listRelatives(node, ap=True)
        }
        files.append(file)
    unique = list(dict.fromkeys([x['path'] for x in files]))
    logger.debug(unique)
    for f in unique:
        logger.info(f'Processing {f}')
        output = convert(f)
        logger.info(output)

    return files


def convert(path, processor_path=None, ocio_path=None):
    cache = os.path.abspath('%LOCALAPPDATA%/Redshift/Cache')
    processor = processor_path if processor_path else r'C:/ProgramData/Redshift/bin/redshiftTextureProcessor.exe'
    ocio = ocio_path if ocio_path else 'L:/resources/ocio/published/aces/lookdev/aces/v001/config_rsCustom.ocio'
    print(path)
    cmd = [processor, path, '-path', os.path.dirname(path), '-noskip', '-ociopath', ocio, '-useociorules']
    print(cmd)
    return subprocess.check_output(cmd)


# os.environ['TMPDIR'] = r'C:\temp'
if __name__ == '__main__':
    main()
