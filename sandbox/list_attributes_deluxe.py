#  1. First select any faces or any object and click the Get checker size button. The checker size is now stored.
#  2. If you want to set the checker size of the whole object click the 'Set Checker size of object(s)' button.
#  3. Otherwise if you want to set the checker size of shells, click the 'Set Checker size of shells' button

#  If 'Face shells' option is selected it will scale the UVs of a shell of faces as a whole, for all the shells
#  If 'UV Shells' option selected it will scale the UVs of a UV shell as a whole, for all the UV shells

#  varun.bondwal@yahoo.com, varun.bondwal@gmail.com. Please report any bugs or suggestions.
#  v1.2 . Modified script to work in Maya 2012, 2013
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import string
import math


def show_window():
    global progressControl
    global current_obj
    global radio_col
    attributes_window = cmds.window(
        title="List Attributes Deluxe",
        iconName='lAttrDX',
        rtf=1,
        s=1,
        widthHeight=(300, 100),
        mxb=0)

    if cmds.window(attributes_window, ex=True):
        cmds.deleteUI(attributes_window, window=True)
    attributes_window = cmds.window(
        title="List Attributes Deluxe",
        iconName='lAttrDX',
        rtf=1,
        s=1,
        widthHeight=(300, 100),
        mxb=0)
    cmds.columnLayout(adjustableColumn=True)

    cmds.frameLayout(label="Get Size", w=30, h=80, mh=5, mw=5, bs="etchedOut")
    cmds.columnLayout(adjustableColumn=True)
    get_attribs_btn = cmds.button(
        label='List attributes',
        en=True,
        annotation='List attributes for selected object',
        command='get_sel_faces_UV_ratio(1)')
    current_obj = cmds.text(w=175, l='', al='center')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.frameLayout(label="Set Size", w=30, h=110, mh=5, mw=5, bs="etchedOut")
    cmds.textScrollList(
        # append=data,
        allowMultiSelection=True,
        # width=window_width,
        enableBackground=False)
    cmds.columnLayout(adjustableColumn=True)
    UV_set_but = cmds.button(
        label='Set Checker Size of object(s)',
        en=True,
        annotation='Change checker size of one or more meshes',
        command='set_UV_ratio(1)')
    UV_shell_but = cmds.button(
        label='Set Checker Size of shells (Single object)',
        en=True,
        annotation='Change checker size of object with several shells',
        command='set_shell_button()')
    cmds.rowLayout(numberOfColumns=2, columnWidth2=(100, 100))
    radio_col = cmds.radioCollection()
    cmds.radioButton('radio_Face', label='Face shells', al='left')
    cmds.radioButton('radio_UV', label='UV shells', al='left')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.columnLayout(adjustableColumn=True)
    progressControl = cmds.progressBar(maxValue=20, width=300)
    cmds.progressBar(progressControl, edit=True, visible=False)
    cmds.text(w=175, l='varunbondwal@yahoo.com  ', al='right')
    cmds.setParent('..')
    cmds.setParent('..')

    cmds.showWindow(attributes_window)


show_window()
