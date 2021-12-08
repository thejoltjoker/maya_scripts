"""
script_import.py

Import a script and run a function in maya.
"""
from importlib import reload


def main():
    from sequence.maya.tools.clayblast import clayblast_submit
    reload(clayblast_submit)
    clayblast_submit.cb_submit()


if __name__ == "__main__":
    main()
