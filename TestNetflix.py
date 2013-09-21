#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
% python TestCollatz.py > TestCollatz.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import netflix_read, netflix_make_cache, netflix_parse, netflix_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        p = netflix_read(r)
        (i, j) = p.next()
        self.assert_(i == 1)
        self.assert_(j == 10)

# ----
# main
# ----

print "TestNetflix.py"
unittest.main()
print "Done."
