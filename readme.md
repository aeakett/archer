About
=====
This is a really hacky attempt to create a scheme to locally archive stuff from the net and capture some metadata about it. Metadata is stored in a text file that lives next to the archived file with a name in the form of ``FILENAME.meta.txt``. File name collisions are handled (probably poorly) by appending a UUID to the file name if it already exists. For the time being, archer is split into two scripts... one to handle html pages and one to handle everything else. The HTML script is split out because in addition to simply downloading the file, it inlines images, css and scripts with ``inliner``. Each of the ``archer`` scripts should read from a seperate archQueue file. The archQueue file should consist of only lines of the following form:

``URL_TO_ARCHIVE LOCAL_FILE_NAME [TAGS]``

The ``LOCAL_FILE_NAME`` should not contain any spaces, and I've not taken any steps to deal with funky characters... limit yourself to numbers, letters, dashes and underscores.

Each time you run an ``archer`` script it will attempt to archive the first line of the specified archQueue. Once it's done it will remove that line from the archQueue and append it to a log file.

One of the things that ``archer`` does it attempt to archive the given file online at webcitation.org. Currently the code that does this assumes that the webcite archiving succeeds. If it fails, things could get squirrely in a number of ways that I can't even fathom. Of particular note, webcitation.org seems to have an unspoken limit on the number of times its web service can be used over a period of time. THis in particular fails fairly silently, and results in an empty web cite id in the metadata file.

Requirements
============
- [``inliner``](https://github.com/remy/inliner)
- ``python``

Known Issues
============
- webcitation.org seems to have an undisclosed limit to the number of times its web service can be used in a given amount of time. This won't cause a fatal error with archer, but it will leave an empty web cite id field in the metadata file.
- ``inliner`` seems to have problems archiving certain pages. archer fials silently when this happens, but what you'll see is that the archived file is empty. This is a [known issue with inliner](https://github.com/remy/inliner/issues/13).

Ideas For Future Work
=====================
- Rewite the shell script parts in python or node.js.
- Figure out a way to have only one archQueue file and one archer script.
- Fix ``inliner`` so that it doesn't die with empty files
- Create a suite of companion scripts to do various things
  - Rename an archived file and its associated metadata file.
  - Check for various types of failure and correct them in an appropriate way (requeue empty archives, retry webciting pages... others?)
- Make ``archer`` able process an entire archQueue.
