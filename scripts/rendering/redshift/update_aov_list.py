#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.mel as mel


def main():
    """docstring for main"""
    mel.eval("redshiftUpdateActiveAovList()")  # refresh the redshift UI


if __name__ == '__main__':
    main()
