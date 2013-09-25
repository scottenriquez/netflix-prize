#!/usr/bin/env python

# -------
# imports
# -------

import sys

from Netflix import netflix_read, netflix_compute_RMSE, netflix_make_cache

# ----
# main
# ----

#ensure that all three caches are given
assert sys.argv[1] != None and sys.argv[2] != None and sys.argv[3] != None
#exact size of cache so resizing is not necessary
#if not found in cache file for some reason, defaults to 2.5 rating
userRatingCache = [2.5] * 2649430
movieRatingCache = [2.5] * 17771
#read caches: average user rating, average movie rating, and answers to Downing's probe file
netflix_make_cache(userRatingCache, open(sys.argv[1], "r"))
netflix_make_cache(movieRatingCache, open(sys.argv[2], "r"))
actualRatingLines = netflix_read(open(sys.argv[3], "r"))
#read probe from system in
#probeLines = netflix_read(sys.stdin)
#read Downing's probe.txt
probeLines = netflix_read(open("/u/downing/cs/netflix/probe.txt", "r"))
#final lines of standard out
print ("RMSE: " + str(netflix_compute_RMSE(probeLines, actualRatingLines, userRatingCache, movieRatingCache)))
