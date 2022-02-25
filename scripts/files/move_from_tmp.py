import os
import re
import maya.cmds as cmds


def moveFromTmp(*args):
    scenename = str((cmds.file(q=1, sn=1)).split('.')[0])
    justfilename = scenename.split('/')[-1]
    imagedir = re.sub('scenes', 'images', os.path.dirname(scenename))

    if os.path.isdir(imagedir):
        if justfilename in ''.join((os.listdir(imagedir))):
            t = cmds.confirmDialog(title='Confirm', message='Found images in folder will be replaced. Are you sure?',
                                   button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            if t == "Yes":
                for x in (os.listdir(imagedir + '/tmp')):
                    if justfilename in x:
                        os.rename(imagedir + '/tmp/' + x, imagedir + "/" + x)

            else:
                print("Cancelled.")
        else:
            for x in (os.listdir(imagedir + '/tmp')):
                if justfilename in x:
                    os.rename(imagedir + '/tmp/' + x, imagedir + "/" + x)
    else:
        cmds.error('No image dir in expected location. Cancelled.')
