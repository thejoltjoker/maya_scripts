import os
import sys
import sys
import maya.cmds as cmds

rendercam = sys.argv[1]
template = sys.argv[2]
anim_file = sys.argv[3]
render_file = sys.argv[4]
min_time = sys.argv[5]
max_time = sys.argv[6]

def cb_import(rendercam, template, anim_file, render_file, min_time, max_time):
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
        maya_file_to_open = template

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
        cmds.file(force=True, save=True, options='v=1;p=17', type='mayaAscii')

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

def cb_test(rendercam, template, anim_file, render_file, min_time, max_time):
    try:
        print "rendercam = "+rendercam
        print "template = "+template
        print "anim_file = "+anim_file
        print "render_file = "+render_file
        print "min_time = "+min_time
        print "max_time = "+max_time
        sys.stdout.write("success")
        return "success"
    except Exception, e:

cb_test(rendercam, template, anim_file, render_file, min_time, max_time)

def addRenderLayer(filename,layername):
    try:
        cmds.file(filename,o=1,f=1)
        newLyr = cmds.createRenderLayer(n=layername,empty=1,makeCurrent=1)
        meshes = cmds.ls(type='mesh')
        xforms = []
        for i in meshes:
            xf = cmds.listRelatives(i,p=1)[0]
            xforms.append(xf)
            cmds.editRenderLayerMembers(layername,xforms)
        cmds.file(s=1,f=1)
        sys.stdout.write(newLyr)
        return newLyr
    except Exception, e:
        sys.stderr.write(str(e))
        sys.exit(-1)
