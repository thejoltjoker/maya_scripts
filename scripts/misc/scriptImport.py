def scriptImport():
    from sequence.maya.tools.clayblast import clayblast_submit
    reload(clayblast_submit)
    clayblast_submit.cb_submit()
    print '# Script reloaded'

scriptImport()