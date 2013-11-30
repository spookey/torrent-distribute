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
        'udp://tracker.ccc.de/announce',
    ],
    'webseeds': [
        'http://images.freifunk.lacerta.uberspace.de/',
        'http://download.crazyhaze.de/ffmz/',
    ],
}

if __name__ == '__main__':
    write_json(configfile, settings)
