#!/bin/bash

webciteEmail='aeakett@gmail.com'
tagOpenDelim='['
tagCloseDelim=']'
archQueueFile=archQueueOther.txt
outputPath=/cygdrive/c/a-stuff/Dropbox/archive/
#record=`head -3 $archQueueFile|tail -1`
#record=`head -2 $archQueueFile|tail -1`
record=`head -1 $archQueueFile`
urlToArchive=`echo $record|awk '{print $1;}'`
uuid=`python -c 'import uuid; print uuid.uuid1()'`
outputFileName=`echo $record|awk '{print $2;}'`
if [ -e "$outputPath$outputFileName" ]
then
   outputFileName=$outputFileName.$uuid
fi
tags=`echo $record|cut -d ' ' -f3-`
dateArchived=`date +'%F %T %z'`

wget $urlToArchive --output-document=$outputPath/$outputFileName

wcid=`./getWebciteID.py "$urlToArchive" "$webciteEmail"`

echo id: $uuid >> $outputPath/$outputFileName.meta.txt
echo webcite id: $wcid >> $outputPath/$outputFileName.meta.txt
echo date archived: $dateArchived >> $outputPath/$outputFileName.meta.txt
echo original url: $urlToArchive >> $outputPath/$outputFileName.meta.txt
echo tags: $tags >> $outputPath/$outputFileName.meta.txt
echo notes: >> $outputPath/$outputFileName.meta.txt

echo $record >> processed.txt
sed -i -e "1d" $archQueueFile