# replace the ";" with ":" for OSX
# or better yet determine your system and
# automatically do it. I'll leave that up to you.
# (hint: try os.name)

import sys
from pymel.all import *


def get_environment():
    script_paths = mel.getenv("MAYA_SCRIPT_PATH")
    plugin_paths = mel.getenv("MAYA_PLUG_IN_PATH")
    python_paths = mel.getenv("PYTHONPATH")
    icon_paths = mel.getenv("XBMLANGPATH")
    path_paths = mel.getenv("PATH")
    sys_paths = sys.path

    allScriptPaths = script_paths.split(";")
    print("\nMAYA_SCRIPT_PATHs are:")
    for scriptPath in allScriptPaths:
        print(scriptPath)

    allPlugInPaths = plugin_paths.split(";")
    print("\nMAYA_PLUG_IN_PATHs are:")
    for plugInPath in allPlugInPaths:
        print(plugInPath)

    allPythonPaths = python_paths.split(";")
    print("\nPYTHONPATHs are:")
    for pythonPath in allPythonPaths:
        print(pythonPath)

    allIconPaths = icon_paths.split(";")
    print("\nXBMLANGPATHs are:")
    for iconPath in allIconPaths:
        print(iconPath)

    allPathPaths = path_paths.split(";")
    print("\nPATHs are:")
    for pathPath in allPathPaths:
        print(pathPath)

    print("\nsys.paths are:")
    for sysPath in sys_paths:
        print(sysPath)
