# Install SOuP on farm
import maya.cmds as cmds
version = cmds.about(v=True)
soup_path = '//SEQ-LIVE/live_projects/_Plugins/Maya/SOuP/plug-ins/maya' + version + '_win'
os.environ['MAYA_PLUG_IN_PATH'] += os.pathsep + soup_path
