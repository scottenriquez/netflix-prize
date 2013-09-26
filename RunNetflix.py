#!/usr/bin/env python

# -------
# imports
# -------

import sys

from Netflix import netflix_read_actual, netflix_read_probe, netflix_compute_RMSE, netflix_make_cache

# ----
# main
# ----

#exact size of cache so resizing is not necessary
#if not found in cache file for some reason, defaults to 2.5 rating
userRatingCache = [2.5] * 2649430
movieRatingCache = [2.5] * 17771
#read caches
netflix_make_cache(userRatingCache, open("/u/lara/cs373-netflix-tests/ghawk88-users_average_rating.txt", "r"))
netflix_make_cache(movieRatingCache, open("/u/lara/cs373-netflix-tests/cmlinac-movies_average_rating.txt", "r"))
actualRatings = netflix_read_actual(open("/u/lara/cs373-netflix-tests/ashorn49-bbell-user_and_rating.txt", "r"))
#read probe from system in
probeLines = netflix_read_probe(sys.stdin)
#compute RMSE
print ("RMSE: " + str(netflix_compute_RMSE(probeLines, actualRatings, userRatingCache, movieRatingCache)))
