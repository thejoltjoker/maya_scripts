import sys
scriptDir = 'C:/johannes/gdrive/scripts/sequence/maya/tools'
if scriptDir not in sys.path:
    sys.path.append(scriptDir)
try:
    reload(exportNulls)
except:
    import exportNulls

exportNulls.exportNulls()




def seqMenuImport():
    import sys
    scriptDir = 'C:/johannes/gdrive/scripts'
    if scriptDir not in sys.path:
        sys.path.append(scriptDir)
    try:
        reload(sequence.maya)
    except:
        from sequence.maya import menu as seqMenu
    seqMenu.theSequenceMenu()
    print '# Sequence menu reloaded'

seqMenuImport()