#!/usr/bin/env python

"""
To test the program:
% python TestNetflix.py > TestNetflix.out
% chmod ugo+x TestNetflix.py
% TestNetflix.py > TestNetflix.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import netflix_read, netflix_make_cache, netflix_estimate_rating, netflix_cache_read

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1:\n35\n233\n")
        lines = netflix_read(r)
        expected = ["1:", "35", "233"]
        self.assert_(lines == expected)

    def test_read_2(self) :
        r = StringIO.StringIO("1:\n35\n233\n34:\n864\n6")
        lines = netflix_read(r)
        expected = ["1:", "35", "233", "34:", "864", "6"]
        self.assert_(lines == expected)

    def test_read_3(self) :
        r = StringIO.StringIO("123456:\n9876\n345\n54:\n86\n")
        lines = netflix_read(r)
        expected = ["123456:", "9876", "345", "54:", "86"]
        self.assert_(lines == expected)

    #-----------
    # make_cache
    #-----------
    def test_make_cache(self) :
        r = StringIO.StringIO("1 4.78\n2 2.345\n3 3.452")
        cache = [-1]*4
        netflix_make_cache(cache, r)
        expected = [-1, 4.78, 2.345, 3.452]
        self.assert_(cache == expected)

    def test_make_cache_2(self) :
        r = StringIO.StringIO("1 4.78\n2 2.345\n3 3.452\n9 67.43\n8 3.65")
        cache = [-1]*10
        netflix_make_cache(cache, r)
        expected = [-1, 4.78, 2.345, 3.452, -1, -1, -1, -1 , 3.65, 67.43]
        self.assert_(cache == expected)

    def test_make_cache_3(self) :
        r = StringIO.StringIO("1 4.78\n2 2.345\n3 3.452\n9 67.43\n8 3.65\n6 23.423\n5 43")
        cache = [-1]*10
        netflix_make_cache(cache, r)
        expected = [-1, 4.78, 2.345, 3.452, -1, 43.0,23.423, -1 , 3.65, 67.43]
        self.assert_(cache == expected)

    #-----------
    # cache_read
    #-----------
    def test_cache_read(self) :
        userCache = [-1, 4.5, 2.5, 3.5, -1, 5.0, 3.0, -1 , 1.0, 4.0]
        movieCache = [-1, 3.5, 5.0, 4.5, 2.5, 3.5, 2.5, 1.5, 3.5, 4.5]
        rating = netflix_cache_read(1, 4, userCache, movieCache)
        expected = 3.5
        self.assert_(rating == expected)

    def test_cache_read_2(self) :
        userCache = [-1, 4.5, 2.5, 3.5, -1, 5.0, 3.0, -1 , 1.0, 4.0]
        movieCache = [-1, 3.5, 5.0, 4.5, 2.5, 3.5, 2.5, 1.5, 3.5, 4.5]
        rating = netflix_cache_read(4, 2, userCache, movieCache)
        expected = 3.75
        self.assert_(rating == expected)

    def test_cache_read_3(self) :
        userCache = [-1, 4.5, 2.5, 3.5, -1, 5.0, 3.0, -1 , 1.0, 4.0]
        movieCache = [-1, 3.5, 5.0, 4.5, 2.5, 3.5, 2.5, 1.5, 3.5, 4.5]
        rating = netflix_cache_read(4, 0, userCache, movieCache)
        expected = 2.5
        self.assert_(rating == expected)
# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
