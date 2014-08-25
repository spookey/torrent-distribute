#!/usr/bin/env python2.7
# -.- coding: utf-8 -.-

from os import listdir
from argparse import ArgumentParser
from bencode import bencode, bdecode
from hashlib import sha1
from base64 import b32encode
from helpers import read_file, write_file, write_json
from datetime import datetime

def get_magnet(torrentfile):
    metadata = bdecode(read_file(torrentfile))
    hashcontents = bencode(metadata['info'])
    digest = sha1(hashcontents).digest()
    return 'magnet:?xt=urn:btih:%s' %(b32encode(digest))

def get_html(mdict):
    result = '<p>\n\t<h2>Magnet Links</h2>\n\n\t<ul>\n'
    for magnet in mdict:
        result += '\t\t<li>\n\t\t\t<a href="%s">%s</a>\n\t\t</li>\n' %(mdict[magnet], magnet)
        print(magnet)
        print(mdict[magnet])
    result += '\t</ul>\n</p><p>last update: %s</p>\n' %(datetime.strftime(datetime.now(), '%d.%m.%y-%H:%M'))
    return result

def parser():
    parser = ArgumentParser(prog='get-magnet', description='get magnet links from existing torrents ~ CLI', epilog='magneto at your service', add_help=True)
    parser.add_argument('input', action='store', help='specify torrents for input')
    parser.add_argument('output', action='store', nargs='?', help='specify output file name')
    return parser.parse_args()

def main():
    args = parser()

    torrentfiles = list()
    magnets = dict()

    source = args.input
    if source.endswith('/') or source.endswith('.'):
        for tfile in listdir(source):
            if tfile.endswith('.torrent'):
                torrentfiles.append(tfile)
    else:
        torrentfiles.append(source)

    for torrent in torrentfiles:
        magnets[torrent] = get_magnet(torrent)

    output = args.output
    if output is None:
        for torrent in magnets:
            print('%s\t%s' %(torrent, magnets[torrent]))
    else:
        if output.endswith('.json'):
            write_json(output, magnets)
        elif output.endswith('.html'):
            write_file(output, get_html(magnets))
        else:
            print('error: output was not correct. use file.{json,html} as parameter')

if __name__ == '__main__':
    main()
