#Torrent-Distribute

##Batch Create Torrents

###Usage

1. Make yourself a config file:

	* Include the *Trackers* and *Webseeds* you want to use in the `mkconf.py` file.
	* Then run the `mkconf.py` file:

			./mkconf.py

	* you should have a `config.json` file afterwards.

2. Create your torrents:

	* example:

			./create_torrents.py ./my-awesome-files/ awesome-files.torrent

		You can use the `--magnet` switch to get the magnet link.

	* see `create_torrents.py --help`.

3. Save the magnet links:

	* example:

			./get_magnet.py ./folder-full-of/torrents magnets.json

		If you leave the output-file (*magnets.json*) you'll get the result in the console.

	* see `get_magnet.py --help`.


###Installation

Check out the repository.
You'll need the `bencode` package for magnet link generation

see `requirements.pip`.

_bencode_ is still python2 only, so we are stuck here.. Written with python3 in mind.

###Bonus

:cow: :pig: :horse:

:smile:
