#!/usr/bin/python

import ConfigParser, os

config= None
for loc in os.curdir, os.path.expanduser("~"), os.environ.get("ARCHERRC"):
    try:
        with open(os.path.join(loc,".archerrc")) as source:
            config.readfp( source )
    except IOError:
        pass

