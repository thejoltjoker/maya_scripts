#!/usr/bin/env python3
"""print_.py
Description of print_.py.
"""
import os
import re
from pathlib import Path
from maya import cmds


def resolve_environment_variables(path: str):
    resolved_path = path
    result = re.findall('\$[\w\d]+', path)
    if result:
        for i in result:
            variable = i.strip('$')
            resolved = os.getenv(variable)
            resolved_path = resolved_path.replace(i, resolved)
    return Path(resolved_path)


def get_sizes(paths: list):
    size = 0
    for path in paths:
        try:
            if path.is_file():
                size += path.stat().st_size
        except Exception as e:
            print(e)

    return size


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def main():
    """docstring for main"""
    paths = []
    path_attributes = ['computedFileNamePattern', 'fileTextureName', 'computedFileTextureNamePattern',
                       'fileTextureNamePattern']
    for node in cmds.ls(r=True):
        for attr in path_attributes:
            if cmds.attributeQuery(attr, node=node, ex=True):
                path = cmds.getAttr(f'{node}.{attr}')
                resolved_path = resolve_environment_variables(path)
                if resolved_path not in paths:
                    paths.append(resolved_path)
                    print(f'{path} -> {resolved_path}')

    print(f'Total {len(paths)} files')
    print(sizeof_fmt(get_sizes(paths)))


if __name__ == '__main__':
    main()
