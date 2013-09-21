#!/usr/bin/env python

"""
To run the program
% python RunNetflix.py < RunNetflix.in > RunNetflix.out
% chmod ugo+x RunNetflix.py
% RunNetflix.py < RunNetflix.in > RunNetflix.out

To document the program
% pydoc -w Netflix
"""

# -------
# imports
# -------

import sys

from Netflix import netflix_read, netflix_estimate_rating, netflix_make_cache

# ----
# main
# ----
assert sys.argv[1] != None and sys.argv[2] != None
#exact size of cache so no resizing is necessary
userRatingCache = [-1] * 2649430
movieRatingCache = [-1] * 17771
#file in
netflix_make_cache(userRatingCache, open(sys.argv[1], "r"))
netflix_make_cache(movieRatingCache, open(sys.argv[2], "r"))
probeLines = netflix_read(open("/u/downing/cs/netflix/probe.txt", "r"))
netflix_estimate_rating(probeLines, userRatingCache, movieRatingCache)
