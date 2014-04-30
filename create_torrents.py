#!/usr/bin/env python2.7
# -.- coding: utf-8 -.-

from argparse import ArgumentParser
from subprocess import Popen
from helpers import read_json, configfile
from get_magnet import get_magnet

def parser():
    parser = ArgumentParser(prog='create-torrents', description='create torrent files from files/folders ~ CLI', epilog='That\'s what she said', add_help=True)
    parser.add_argument('input', action='store', help='specify input files/folders')
    parser.add_argument('output', action='store', nargs='?', help='specify output folder')
    parser.add_argument('--magnet', '-m', action='store_true', help='should I create magnet links?')
    return parser.parse_args()

def main():
    config = read_json(configfile)
    if config is not None:

        args = parser()

        trackers = ','.join(config['trackers'])
        webseeds = ','.join(config['webseeds'])

        output = args.output

        if output is None:
            if '/' in args.input:
                t = args.input.split('/')
                output = t[-2] if t[-1] is '' else t[-1] #trailing slash
            else:
                output = '%s.torrent' %(args.input)

        if not output.endswith('.torrent'):
            output += '.torrent'

        print('\ncreating torrent for %s:' %(args.input))
        p = Popen([config['mktorrent'], '-a', trackers, '-w', webseeds, '-o', output, '-c', '%s' %(config['comment']), args.input])
        p.communicate()
        print('done')
        if args.magnet:
            print('magnet link: %s' %(get_magnet(output)))

    else:
        print('Error: Could not read from config file %s. Does it exist? Is the json valid?' %(configfile))

if __name__ == '__main__':
    main()
