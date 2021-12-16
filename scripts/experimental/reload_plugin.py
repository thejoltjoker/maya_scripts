def seqMenuImport():
    from sequence.maya import menu as seqMenu
    reload(seqMenu)
    seqMenu.theSequenceMenu()
    print '# Sequence menu reloaded'


seqMenuImport()
