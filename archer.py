#!/usr/bin/python

import ConfigParser, os

config = ConfigParser.RawConfigParser()
for loc in os.curdir, os.path.expanduser("~"), os.environ.get("ARCHERRC"):
   try:
      with open(os.path.join(loc, ".archerrc")) as source:
         config.readfp( source )
   except (IOError, AttributeError) as e:
      pass

print config.get("archer", "webciteEmail")
print config.get("archer", "archQueueFile")
print config.get("archer", "outputPath")