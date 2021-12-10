#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
from Deadline.DeadlineConnect import DeadlineCon as Connect

def main():
    """docstring for main"""
    con = Connect('WebServiceName', 8081)
    con.Groups.GetGroupNames()

if __name__ == '__main__':
    main()