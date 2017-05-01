import maya.standalone
print "Imported maya.standalone"

# Initialize maya standalone
maya.standalone.initialize(name='python')
print "Maya Standalone Initialized"

# Do maya stuff here
import sys
import os
import maya.cmds as cmds

# Variables
# test_out = sys.argv[1]
rendercam = sys.argv[1]
template = sys.argv[2]
anim_file = sys.argv[3]
render_file = sys.argv[4]
min_time = sys.argv[5]
max_time = sys.argv[6]



# List the plugins that are currently loaded
plugins = cmds.pluginInfo(query=True, listPlugins=True)
# Load Redshift
if "redshift4maya" in plugins:
    print "Redshift is already loaded."
else:
    cmds.loadPlugin('redshift4maya')
    print "Redshift is now loaded."

# full path to your Maya file to OPEN
maya_file_to_open = r"P:/sequence_rnd_02/sequences/001/clayblast/Rendering/work/maya/clayblast_Rendering_Template_v001.ma"

# full path to your Maya file to IMPORT
maya_file_to_import = r"P:/sequence_rnd_02/sequences/001/clayblast/Lay/work/maya/clayblast_Lay_v001.ma"

render_file = r"C:/mayapyTest/"+test_out+".ma"
# Have a namespace if you want (recommended)
namespace = "anim"

cmds.file(maya_file_to_open, o=True)

# Import the file. the variable "nodes" will hold the names of all nodes imported, just in case.
nodes = cmds.file(maya_file_to_import, i=True, renameAll=True, mergeNamespacesOnClash=False, namespace=namespace, returnNewNodes=True, options="v=0;")

cmds.file(rename=render_file)
cmds.file(force=True, save=True, type='mayaAscii')

print "File Saved"

print "Submitting to Deadline"

deadline_path = 'C:/Program Files/Thinkbox/Deadline9/bin/deadlinecommand.exe'
scene_file = render_file
command = '"%s" "%s "' %(deadline_path, scene_file)
os.system('"' + command + '"')

maya.standalone.uninitialize()

exit()