#!/usr/bin/env python
# -.- coding: utf-8 -.-

from helpers import write_json, configfile

settings = {
    'mktorrent': '/usr/bin/mktorrent',
    'comment': 'your mom',
    'trackers': [
        'udp://tracker.openbittorrent.com:80/announce',
        'http://tracker.openbittorrent.com:80/announce',
        'udp://tracker.publicbt.com:80/announce',
        'http://tracker.publicbt.com:80/announce',
        'http://tracker.ccc.de/announce',
        'udp://tracker.ccc.de:80/announce',
    ],
    'webseeds': [
        'http://webseed.example.com/',
    ],
}

if __name__ == '__main__':
    write_json(configfile, settings)
