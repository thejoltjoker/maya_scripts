import maya.standalone

print "imported maya.standalone"

maya.standalone.initialize(name='python')
print "Maya Standalone Initialized"

# DO MAYA STUFF HERE
import sys
import maya.cmds as cmds

# VARIABLES
try:
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

    render_file = r"C:/mayapyTest/submission.ma"
    # Have a namespace if you want (recommended)
    namespace = "anim"

    cmds.file(maya_file_to_open, o=True)

    # Import the file. the variable "nodes" will hold the names of all nodes imported, just in case.
    nodes = cmds.file(maya_file_to_import, i=True, renameAll=True, mergeNamespacesOnClash=False, namespace=namespace, returnNewNodes=True, options="v=0;")

    cmds.file(rename=render_file)
    cmds.file(force=True, save=True, type='mayaAscii')

    print "File Saved"

    sys.stdout.write(render_file)
    return render_file

except Exception, e:
    sys.stderr.write(str(e))
    sys.exit(-1)



maya.standalone.uninitialize()

exit()