"""
This script will submit current file to deadline for render
"""
import os
import sys
import subprocess
import maya.cmds as cmds


def maya_deadline_job():
    """
    this function will collect scene file information and write a job file
    :return:
    """
    renderer_name = 'File'
    version = cmds.about(version=True)
    project_path = cmds.workspace(q=True, directory=True)
    width = cmds.getAttr("defaultResolution.width")
    height = cmds.getAttr("defaultResolution.height")
    output_file_path = cmds.workspace(expandName="images")
    output_file_prefix = cmds.getAttr("defaultRenderGlobals.imageFilePrefix")
    scene_file = cmds.file(q=True, location=True)
    info_txt = 'Animation=1\n' \
               'Renderer={}\n' \
               'UsingRenderLayers=0\n' \
               'RenderLayer=\n' \
               'RenderHalfFrames=0\n' \
               'LocalRendering=0\n' \
               'StrictErrorChecking=1\n' \
               'MaxProcessors=0\n' \
               'AntiAliasing=low\n' \
               'Version={}\n' \
               'Build=64bit\n' \
               'ProjectPath={}\n' \
               'ImageWidth={}\n' \
               'ImageHeight={}\n' \
               'OutputFilePath={}\n' \
               'OutputFilePrefix={}\n' \
               'Camera=\n' \
               'Camera0=\n' \
               'Camera1=RENDERShape\n' \
               'Camera2=frontShape\n' \
               'Camera3=perspShape\n' \
               'Camera4=sideShape\n' \
               'Camera5=topShape\n' \
               'SceneFile={}\n' \
               'IgnoreError211=0'.format(renderer_name,
                                         version,
                                         project_path,
                                         width,
                                         height,
                                         output_file_path,
                                         output_file_prefix,
                                         scene_file)

    maya_deadline_job_file = r'{}\maya_deadline_job.job'.format(os.getenv('TEMP'))
    with open(maya_deadline_job_file, 'w') as job_file:
        job_file.write(info_txt)
    return maya_deadline_job_file


def maya_deadline_info():
    """
    this function will collect maya deadline information and write a job file
    :return:
    """
    info_txt = 'Plugin=MayaBatch\n' \
               'Name=MY_FILE_NAME\n' \
               'Comment=Render Launch by Python\n' \
               'Pool=none\n' \
               'MachineLimit=0\n' \
               'Priority=50\n' \
               'OnJobComplete=Nothing\n' \
               'TaskTimeoutMinutes=0\n' \
               'MinRenderTimeMinutes=0\n' \
               'ConcurrentTasks=1\n' \
               'Department=\n' \
               'Group=none\n' \
               'LimitGroups=\n' \
               'JobDependencies=\n' \
               'InitialStatus=Suspended\n' \
               'OutputFilename0=C:/Users/raijv/Documents/maya/projects/default/images/masterLayer_2.iff.????\n' \
               'Frames=1-10\n' \
               'ChunkSize=1'

    maya_deadline_info_file = r'{}\maya_deadline_info.job'.format(os.getenv('TEMP'))
    with open(maya_deadline_info_file, 'w') as job_file:
        job_file.write(info_txt)
    return maya_deadline_info_file


def submit_to_deadline():
    """
    this function will send current scene to deadline for rendering
    :return:
    """
    deadline_cmd = r"C:\Program Files\Thinkbox\Deadline\bin\deadlinecommand.exe"
    job_file = maya_deadline_job()
    info_file = maya_deadline_info()
    command = '{deadline_cmd} "{job_file}" "{info_file}"'.format(**vars())
    os.system('"' + command + '"')

submit_to_deadline()