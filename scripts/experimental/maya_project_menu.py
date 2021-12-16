import maya.cmds as cmds
import maya.mel as mel
import os

def create():

    cmds.deleteUI('customMenu')

    cmds.menu('customMenu', allowOptionBoxes=True, parent='MayaWindow', label='Project Menu', tearOff=True)

    cmds.menuItem(label='PROJECTS', en=False)
    cmds.menuItem(divider=True )
    cmds.menuItem(subMenu=True, label='shark', tearOff=True)
    cmds.menuItem(label='Open lookdev scene', c=shark_lookdev)
    cmds.menuItem(label='Open model scene', c=shark_model, en=False)
    cmds.menuItem(subMenu=True, label='Animation')
    cmds.menuItem(label='sh010 (swim)', c=shark_anim_sh010)
    cmds.menuItem(label='sh020 (jump)', c=shark_anim_sh020)

    cmds.setParent( '..', menu=True )
    cmds.setParent( '..', menu=True )

    cmds.menuItem(subMenu=True, label='guitar', tearOff=True)
    cmds.menuItem(label='Open latest scene', c=instrument_work)

    cmds.setParent( '..', menu=True )

    cmds.menuItem(subMenu=True, label='Game Boy', tearOff=True)
    cmds.menuItem(label='Open latest scene', c=gba_work)

    cmds.setParent( '..', menu=True )

    cmds.menuItem(subMenu=True, label='velociraptor', tearOff=True)
    cmds.menuItem(label='Open lookdev scene', c=raptor_lookdev)
    cmds.menuItem(label='Open animation scene', c=raptor_animation)

# functions
def shark_lookdev():
    sharkLookdevPath = "Q:/DV14/Work/johannesAndersson/0040_shark/assets/creatures/shark/lookdev/work/maya"
    mel.eval('setProject '+sharkLookdevPath+';')
    print sharkLookdevPath
    files = os.listdir(sharkLookdevPath+'/scenes')
    latestFile = max(files)
    cmds.file(latestFile, o=True)
    print latestFile
    return

def shark_model(*args):
    sharkModelPath = "Q:/DV14/Work/johannesAndersson/0040_shark/assets/creatures/shark/model/work/maya"
    mel.eval('setProject "' + str(sharkModelPath) + '";')
    print sharkModelPath
    files = os.listdir(sharkModelPath+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return

def shark_anim_sh010(*args):
    sharkAnimSh010Path = "Q:/DV14/Work/johannesAndersson/0040_shark/sequences/sq010/sh010/animation/work/maya"
    mel.eval('setProject "' + str(sharkAnimSh010Path) + '";')
    files = os.listdir(sharkAnimSh010Path+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return

def shark_anim_sh020(*args):
    sharkAnimSh020Path = "Q:/DV14/Work/johannesAndersson/0040_shark/sequences/sq010/sh020/animation/work/maya"
    mel.eval('setProject "' + str(sharkAnimSh020Path) + '";')
    files = os.listdir(sharkAnimSh020Path+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return

def gba_work(*args):
    gbaWorkPath = "Q:/DV14/Work/johannesAndersson/2014_034_ci12_gba/gameBoyAdvance_lameBoys"
    mel.eval('setProject "' + str(gbaWorkPath) + '";')
    print gbaWorkPath
    files = os.listdir(gbaWorkPath+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return

def raptor_lookdev(*args):
    raptorLookdevPath = "Q:/DV14/Work/johannesAndersson/0015_ci12_timeTravel/3d/assets/velociraptor/work/shading/breakdown"
    mel.eval('setProject "' + str(raptorLookdevPath) + '";')
    print raptorLookdevPath
    files = os.listdir(raptorLookdevPath+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return

def raptor_animation(*args):
    raptorAnimationPath = "Q:/DV14/Work/johannesAndersson/0015_ci12_timeTravel/3d/assets/velociraptor/work/animation/breakdown"
    mel.eval('setProject "' + str(raptorAnimationPath) + '";')
    print raptorAnimationPath
    files = os.listdir(raptorAnimationPath+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return


def instrument_work(*args):
    instrumentWorkPath = "Q:/DV14/HT15_2_3D_III_Look_Development/johannesAndersson/2014_030_ci12_instrument/assets/fenderStratocaster/model/work/maya"
    mel.eval('setProject "' + str(instrumentWorkPath) + '";')
    print instrumentWorkPath
    files = os.listdir(instrumentWorkPath+'/scenes')
    latestFile = max(files)
    cmds.file( latestFile, o=True, force=True )
    print latestFile
    return

create()