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

from Netflix import netflix_read_actual, netflix_read_probe, netflix_compute_RMSE, netflix_make_cache, netflix_estimate_rating

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :
    # ----------
    # read_probe
    # ----------

    def test_read_probe (self) :
        r = StringIO.StringIO("1:\n35\n233\n")
        lines = netflix_read_probe(r)
        expected = ["1:", "35", "233"]
        self.assert_(lines == expected)

    def test_read_probe2 (self) :
        r = StringIO.StringIO("1:\n35\n233\n34:\n864\n6")
        lines = netflix_read_probe(r)
        expected = ["1:", "35", "233", "34:", "864", "6"]
        self.assert_(lines == expected)

    def test_read_probe3 (self) :
        r = StringIO.StringIO("123456:\n9876\n345\n54:\n86\n")
        lines = netflix_read_probe(r)
        expected = ["123456:", "9876", "345", "54:", "86"]
        self.assert_(lines == expected)

    #-----------
    # make_cache
    #-----------

    def test_make_cache(self) :
        r = StringIO.StringIO("1 4.78\n2 2.345\n3 3.452")
        cache = [-1] * 4
        netflix_make_cache(cache, r)
        expected = [-1, 4.78, 2.345, 3.452]
        self.assert_(cache == expected)

    def test_make_cache_2(self) :
        r = StringIO.StringIO("1 4.78\n2 2.345\n3 3.452\n9 4.43\n8 3.65")
        cache = [-1] * 10
        netflix_make_cache(cache, r)
        expected = [-1, 4.78, 2.345, 3.452, -1, -1, -1, -1 , 3.65, 4.43]
        self.assert_(cache == expected)

    #checks typecasting
    def test_make_cache_3(self) :
        r = StringIO.StringIO("1 4.78\n2 2.345\n3 3.452\n9 4.43\n8 3.65\n6 3.423\n5 3")
        cache = [-1] * 10
        netflix_make_cache(cache, r)
        expected = [-1, 4.78, 2.345, 3.452, -1, 3.0, 3.423, -1 , 3.65, 4.43]
        self.assert_(cache == expected)

    #------------
    # read_actual
    #------------

    #NOTE: due to loop semantics, the 0th element will be an empty dictionary
    def test_read_actual(self) :
        r = StringIO.StringIO("1:\n1 3.25\n2 4.5")
        cache = [None] * 4
        netflix_read_actual(cache, r)
        expected = [{}, {1 : 3.25, 2 : 4.5}, None, None]
        self.assert_(cache == expected)

    def test_read_actual_2(self) :
        r = StringIO.StringIO("1:\n1 3.25\n2 4.5\n 2:\n 4 2.5")
        cache = [None] * 4
        netflix_read_actual(cache, r)
        expected = [{}, {1 : 3.25, 2 : 4.5}, {4 : 2.5}, None]
        self.assert_(cache == expected)

    def test_read_actual_3(self) :
        r = StringIO.StringIO("1:\n1 3.25\n2 4.5")
        cache = [None] * 4
        netflix_read_actual(cache, r)
        expected = [{}, {1 : 3.25, 2 : 4.5}, None, None]
        self.assert_(cache == expected)

    #-------------
    # compute_RMSE
    #-------------

    def test_compute_RMSE (self) :
        probeLines = ["1:", "1", "2", "3", "2:", "1", "2", "3", "3:", "1", "2", "3"]
        actualRatings = [{}, {1 : 4, 2 : 4, 3 : 4}, {1 : 4, 2 : 4, 3 : 4}, {1 : 4, 2 : 4, 3 : 4}]
        userRatingCache = [-1, 4.0, 4.0, 4.0]
        movieRatingCache = [-1, 4.0, 4.0, 4.0]
        testRMSE = netflix_compute_RMSE (probeLines, actualRatings, userRatingCache, movieRatingCache)
        expected = 0.3767
        self.assert_(str(testRMSE) == str(expected))

    def test_compute_RMSE_2 (self) :
        probeLines = ["1:", "1", "2", "3", "2:", "1", "2", "3", "3:", "1", "2", "3"]
        actualRatings = [{}, {1 : 4, 2 : 4, 3 : 4}, {1 : 4, 2 : 4, 3 : 4}, {1 : 4, 2 : 4, 3 : 4}]
        userRatingCache = [-1, 2.0, 4.5, 5.0]
        movieRatingCache = [-1, 3.0, 4.0, 4.5]
        testRMSE = netflix_compute_RMSE (probeLines, actualRatings, userRatingCache, movieRatingCache)
        expected = 1.27820696203
        self.assert_(str(testRMSE) == str(expected))

    def test_compute_RMSE_3 (self) :
        probeLines = ["1:", "1", "2", "3", "2:", "1", "2", "3", "3:", "1", "2", "3"]
        actualRatings = [{}, {1 : 4, 2 : 4, 3 : 4}, {1 : 4, 2 : 4, 3 : 4}, {1 : 4, 2 : 4, 3 : 4}]
        userRatingCache = [-1, 5.0, 4.0, 3.0]
        movieRatingCache = [-1, 3.0, 4.0, 5.0]
        testRMSE = netflix_compute_RMSE (probeLines, actualRatings, userRatingCache, movieRatingCache)
        expected = 0.871640684125
        self.assert_(str(testRMSE) == str(expected))

    #----------------
    # estimate_rating
    #----------------

    def test_estimate_rating (self) :
        userRatingCache = [-1, 4.0, 4.0, 4.0]
        movieRatingCache = [-1, 4.0, 4.0, 4.0]
        estimate = netflix_estimate_rating (1, 2, userRatingCache, movieRatingCache)      
        expected = 4.3767
        self.assert_(str(estimate) == str(expected))

    def test_estimate_rating (self) :
        userRatingCache = [-1, 2.0, 4.5, 5.0]
        movieRatingCache = [-1, 3.0, 4.0, 4.5]
        estimate = netflix_estimate_rating (3, 2, userRatingCache, movieRatingCache)       
        expected = 4.3767
        self.assert_(str(estimate) == str(expected))
    
    #test upper bound
    def test_estimate_rating (self) :
        userRatingCache = [-1, 5.0, 4.0, 3.0]
        movieRatingCache = [-1, 3.0, 4.0, 5.0]
        estimate = netflix_estimate_rating (1, 3, userRatingCache, movieRatingCache)       
        expected = 5.0
        self.assert_(str(estimate) == str(expected))

# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
