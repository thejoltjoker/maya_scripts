#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
alt_load_script.py
Load a script/module
"""

import imp

foo = imp.load_source('maya', 'D:/people/johannes/scripts/repos/sequence/maya/menu.py')
maya.theSequenceMenu()