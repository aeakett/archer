#!/usr/bin/python

# expects getwebciteID.py urlToArchive emailAddress
# adapted from http://www.travisglines.com/web-coding/python-xml-parser-tutorial

import sys
# import library to do http requests:
import urllib2
# import easy to use xml parser called minidom:
from xml.dom.minidom import parseString

# put arguments in variables
urlToArchive = sys.argv[1]
emailAddress = sys.argv[2]

# download the file:
file = urllib2.urlopen('http://www.webcitation.org/archive?returnxml=true&url='+urlToArchive+'&email='+emailAddress)

# convert to string:
data = file.read()
# close file because we dont need it anymore:
file.close()
# parse the xml you downloaded
dom = parseString(data)
# retrieve the first xml tag (<webcite_id_short>data</webcite_id_short>) that the parser finds with name tagName:
xmlTag = dom.getElementsByTagName('webcite_id_short')[0].toxml()
# strip off the tag (<webcite_id_short>data</webcite_id_short>  --->   data):
xmlData=xmlTag.replace('<webcite_id_short>','').replace('</webcite_id_short>','')
# just print the data
print xmlData