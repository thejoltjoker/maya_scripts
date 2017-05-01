import maya.standalone
maya.standalone.initialize( name='python' )
import os
import sys
import sys
import maya.cmds as cmds

def cb_import():
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

        # Have a namespace if you want (recommended)
        namespace = "anim"

        # Import the file. the variable "nodes" will hold the names of all nodes imported, just in case.
        nodes = cmds.file(maya_file_to_import, i=True,
                                renameAll=True,
                                mergeNamespacesOnClash=False,
                                namespace=namespace,
                                returnNewNodes=True,
                                options="v=0;"
                                )

        cmds.file(rename=render_file)
        cmds.file(force=True, save=True, type='mayaAscii')

        sys.stdout.write(render_file)
        return render_file

        # Submission
        # import sys
        # from os import path
        # from subprocess import Popen

        # render_project = r"P:/sequence_rnd_02/sequences/001/clayblast/Rendering/work/maya/images"
        # renderer_folder = path.split(sys.executable)[0]
        # renderer_exec_name = "Render"
        # params = [renderer_exec_name]
        # params += ['-percentRes', '75']
        # params += ['-alpha', '0']
        # params += ['-proj', render_project]
        # params += ['-r', 'mr']
        # params += [render_file]
        # p = Popen(params, cwd=renderer_folder)
        # stdout, stderr = p.communicate()

    except Exception, e:
        sys.stderr.write(str(e))
        sys.exit(-1)

cb_import()