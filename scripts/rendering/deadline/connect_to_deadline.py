#!/usr/bin/env python
"""
connect_to_shotgun.py
Description of connect_to_shotgun.py.
"""
from Deadline.DeadlineConnect import DeadlineCon as Connect


def main():
    """docstring for main"""
    con = Connect('PulseName', 8080)
    con.Groups.GetGroupNames()
    con.AuthenticationModeEnabled()
    con.EnabledAuthentication(True)
    con.AuthenticationModeEnabled()
    con.SetAuthenticationCredentials("username", "password")
    con.Groups.GetGroupNames()


if __name__ == '__main__':
    main()