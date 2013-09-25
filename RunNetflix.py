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

from Netflix import netflix_read, netflix_compute_RMSE, netflix_make_cache

# ----
# main
# ----
assert sys.argv[1] != None and sys.argv[2] != None and sys.argv[3] != None
#exact size of cache so no resizing is necessary
userRatingCache = [2.5] * 2649430
movieRatingCache = [2.5] * 17771
#file in
netflix_make_cache(userRatingCache, open(sys.argv[1], "r"))
netflix_make_cache(movieRatingCache, open(sys.argv[2], "r"))
actualRatingLines = netflix_read(open(sys.argv[3], "r"))
#probeLines = netflix_read(sys.stdin)
#probeLines = netflix_read(open("TestProbe.txt", "r"))
probeLines = netflix_read(open("/u/downing/cs/netflix/probe.txt", "r"))
print ("RMSE: " + str(netflix_compute_RMSE(probeLines, actualRatingLines, userRatingCache, movieRatingCache)))
