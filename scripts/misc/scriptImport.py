def scriptImport():
    from sequence.maya.tools.clayblast import clayblast_submit
    reload(clayblast)
    clayblast_submit.cb_submit()
    print '# Script reloaded'

scriptImport()