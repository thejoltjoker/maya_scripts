#!/usr/bin/env python3
"""toggl_time_tracking.py
Description of tracker.py.
"""
from base64 import b64encode


# from urllib.request import urlopen, Request
#
# httprequest = Request(url, headers={"Accept": "application/json"})
#
# with urlopen(httprequest) as response:
#     print(response.status)
#     print(response.read().decode())


class Toggl:
    def __init__(self):
        self.headers = {}
        self.endpoints = {
            'workspaces': "https://api.track.toggl.com/api/v8/workspaces",
            'clients': "https://api.track.toggl.com/api/v8/clients",
            'projects': "https://api.track.toggl.com/api/v8/projects",
            'tasks': "https://api.track.toggl.com/api/v8/tasks",
            'report_weekly': "https://api.track.toggl.com/reports/api/v2/weekly",
            'report_detailed': "https://api.track.toggl.com/reports/api/v2/details",
            'report_summary': "https://api.track.toggl.com/reports/api/v2/summary",
            'start_time': "https://api.track.toggl.com/api/v8/time_entries/start",
            'time_entries': "https://api.track.toggl.com/api/v8/time_entries",
            'current_running_time': "https://api.track.toggl.com/api/v8/time_entries/current"
        }

    def set_api_key(self, api_key):
        # craft the Authorization
        auth_header = api_key + ':' + 'api_token'
        auth_header = "Basic " + b64encode(auth_header.encode()).decode('ascii').rstrip()

        # add it into the header
        self.headers['Authorization'] = auth_header


def main():
    """docstring for main"""
    pass


if __name__ == '__main__':
    main()
