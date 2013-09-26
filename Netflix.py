# ------------
# netflix_make_cache
# ------------

def netflix_make_cache (cache, fileObject) :
    """
    cache is a pointer to the list to build the cache in
    fileObject is the input cache file
    """    
    for line in fileObject: 
        line = line.strip()
        (itemID, rating) = line.split(" ")
        assert float(rating) >= 1.0 and float(rating) <= 5.0
        cache[int(itemID)] = float(rating)
    fileObject.close()

# ------------
# netflix_read
# ------------

def netflix_read (fileObject) :
    """
    fileObject is for the probe input
    """    
    lines = [line.strip() for line in fileObject]
    fileObject.close()
    return lines

# -----------------------
# netflix_estimate_rating
# -----------------------

def netflix_compute_RMSE (probeLines, actualLines, userRatingCache, movieRatingCache) :
    """
    summation of the difference between our estimate and the actual ratings
    writes our estimates to output file
    """
    currentMovieID = 0
    actualLinesIndex = 0
    sumRMSE = 0.0
    totalRatings = 0
    for probeLine in probeLines :
        #if line containing a movie ID number
        if (probeLine[len(probeLine) - 1] == ":") :
            #make sure the probe and actual rating files are of the same format
            assert actualLines[actualLinesIndex][len(probeLine) - 1] == ":"
            currentMovieID = int(probeLine[0 : len(probeLine) - 1])
            #print (probeLine)
        else :
            currentUserID = int(probeLine)
            estimate = netflix_estimate_rating(currentUserID, currentMovieID, userRatingCache, movieRatingCache)
            assert estimate >= 1.0 and estimate <= 5.0
            sumRMSE += (estimate - float(actualLines[actualLinesIndex])) ** 2
            totalRatings += 1
            #print (str(estimate))
        actualLinesIndex += 1
    return (sumRMSE / totalRatings) ** 0.5

# ------------------
# netflix_cache_read
# ------------------

def netflix_estimate_rating (currentUserID, currentMovieID, userRatingCache, movieRatingCache) :
    """
    overall average rating + user offset + movie offset
    """    
    overallAverage = 3.6233
    estimate = overallAverage + (userRatingCache[currentUserID] - overallAverage) + (movieRatingCache[currentMovieID] - overallAverage)
    if (estimate < 1.0) :
        estimate = 1.0
    if (estimate > 5.0) :
        estimate = 5.0
    return estimate
