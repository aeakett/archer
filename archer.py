#!/usr/bin/python

import ConfigParser, os, uuid, datetime, sys

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







# read first line of archQueueFile

# parse queue line










# generate uuid
archUuid = uuid.uuid1()

# date of archival
archDateTime = datetime.datetime.now()

print archDateTime.strftime("%Y-%m-%d %H:%M")
print archUuid








sys.exit(0)
