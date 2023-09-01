#!/usr/bin/env python3
"""redshift_licensing.py
Description of redshift_licensing.py.
"""
import subprocess
import sys


MX1_PATH = None
if sys.platform == 'win32':
    MX1_PATH = r'C:\Program Files\Maxon\Tools\mx1.exe'

def assign_license():
    subprocess.check_output()
def main():
    """docstring for main"""
    pass


if __name__ == '__main__':
    main()
