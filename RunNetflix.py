#!/usr/bin/env python

"""
To run the program
% python RunCollatz.py < RunCollatz.in > RunCollatz.out
% chmod ugo+x RunCollatz.py
% RunNetflix.py < RunCollatz.in > RunCollatz.out

To document the program
% pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from Netflix import netflix_read, netflix_parse

# ----
# main
# ----

assert sys.argv[1] != None and sys.argv[2] != None
userRatingCache = netflix_read(sys.argv[1])
movieRatingCache = netflix_read(sys.argv[2])
probeLines = netflix_read("/u/downing/cs/netflix/probe.txt")
netflix_parse(probeLines, userRatingCache, movieRatingCache)
