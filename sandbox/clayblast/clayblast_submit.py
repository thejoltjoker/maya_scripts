import os
import maya.cmds as cmds
# from sequence.maya.tools.clayblast import clayblast_import

# def cb_submit():

# Set first frame
min_time = cmds.playbackOptions(q=True, minTime=True)

# Set last frame
max_time = cmds.playbackOptions(q=True, maxTime=True)

# Set camera name
camera = "animation:RENDERCAM"

# Set template file name
render_file_template = r"P:/sequence_rnd_02/sequences/001/clayblast/Rendering/work/maya/clayblast_Rendering_Template_v001.ma"

# Make a new filename based on current filename
cur_file_name = cmds.file(q=True, sn=True, shn=True)
cur_file_name_short = cmds.file(q=True, sn=True, shn=True)
split_cur_file_name = cur_file_name_short.rsplit('_', 1)
scene_task = "Clay"
split_cur_file_name.insert(-1, scene_task)
sep = "_"

# Set render file name
render_file_name = sep.join(split_cur_file_name)

# Set project folder
project_folder = cmds.workspace(q=True, dir=True)

# def submitClayRender(rendercam, template, render_file_name, min_time, max_time):
#     mayaBatchLocation = 'D:/software/Autodesk/Maya2016/bin/mayabatch'
#     command = '"%s" -prompt -batch -file "%s" -script "%s"' %(mayaBatchLocation, template, script)
#     os.system('"' + command + '"')



    # clayblast_import.cb_test(camera, render_file_template, cur_file_name, render_file_name, min_time, max_time)

# import subprocess
# replace mayaPath with the path on your system to mayapy.exe
mayaPath = 'C:/Program Files/Autodesk/Maya2016/bin/mayapy.exe'
# replace scriptPath with the path to the script you just saved
scriptPath = 'D:/people/johannes/scripts/repos/sequence/maya/tools/clayblast/clayblast_import2.py'

def claySubmitter(camera, render_file_template, cur_file_name, render_file_name, min_time, max_time):

    maya = subprocess.Popen(mayaPath+' '+scriptPath+' '+camera+' '+str(render_file_template)+' '+str(cur_file_name)+' '+str(render_file_name)+' '+str(min_time)+' '+str(max_time),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err = maya.communicate()
    exitcode = maya.returncode
    if str(exitcode) != '0':
        print(err)
        print 'error opening file: %s' % (filename)
    else:
        print 'added new layer %s to %s' % (out,filename)

def claySubmitter2():

    mayaBatchLocation = 'C:/Program Files/Autodesk/Maya2016/bin/mayapy.exe'
    file = 'P:/sequence_rnd_02/sequences/001/clayblast/Rendering/work/maya/clayblast_Rendering_Template_v001.ma'
    script = 'D:/people/johannes/scripts/repos/sequence/maya/tools/clayblast/test01.py'
    command = '"%s" "%s"' %(mayaBatchLocation, script)
    os.system('"' + command + '"')

claySubmitter2()