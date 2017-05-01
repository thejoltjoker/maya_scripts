"""
script_import.py

Import a script and run a function in maya.
"""
def scriptImport():
    from sequence.maya.tools.clayblast import clayblast_submit
    reload(clayblast_submit)
    clayblast_submit.cb_submit()
    print '# Script reloaded'

if __name__ == "__main__":
    scriptImport()