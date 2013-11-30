#!/usr/bin/env python
# -.- coding: utf-8 -.-

from os import listdir
from argparse import ArgumentParser
from bencode import bencode, bdecode
from hashlib import sha1
from base64 import b32encode
from helpers import read_file, write_json

def get_magnet(torrentfile):
    metadata = bdecode(read_file(torrentfile))
    hashcontents = bencode(metadata['info'])
    digest = sha1(hashcontents).digest()
    return 'magnet:?xt=urn:btih:%s' %(b32encode(digest))

def parser():
    parser = ArgumentParser(prog='get-magnet', description='get torrent magnet links for files/folders ~ CLI', epilog='That\'s what she said', add_help=True)
    parser.add_argument('input', action='store', help='specify input files/folders')
    parser.add_argument('output', action='store', nargs='?', help='specify output file')
    return parser.parse_args()

def main():
    args = parser()

    torrentfiles = list()
    magnets = dict()

    source = args.input

    if source.endswith('/') or '.':
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
        if not output.endswith('.json'):
            output += '.json'
        write_json(output, magnets)


if __name__ == '__main__':
    main()
