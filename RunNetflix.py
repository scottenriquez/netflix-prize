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

from Netflix import netflix_read, netflix_parse, netflix_make_cache

# ----
# main
# ----
userRatingCache = [-1]*2649430
movieRatingCache = [-1]*17771
assert sys.argv[1] != None and sys.argv[2] != None
netflix_make_cache(userRatingCache, sys.argv[1])
netflix_make_cache(movieRatingCache, sys.argv[2])
num = 0
while num < 20:
    print(userRatingCache[num])
    #print(movieRatingCache[num])
    num+=1;
probeLines = netflix_read("/u/downing/cs/netflix/probe.txt")
netflix_parse(probeLines, userRatingCache, movieRatingCache)
