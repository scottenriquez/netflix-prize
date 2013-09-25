# ------------
# netflix_make_cache
# ------------

def netflix_make_cache (cache, fileObject) :
    """
    
    """    
    for line in fileObject: 
        line = line.strip()
        (i, j) = line.split(" ")
        cache[int(i)] = float(j)

# ------------
# netflix_read
# ------------

def netflix_read (fileObject) :
    """
    fileObject is the probe.txt file
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
        if(probeLine[len(probeLine) - 1] == ":") :
            #ensuring that the probe and actual rating files are of the same format
            assert actualLines[actualLinesIndex][len(probeLine) - 1] == ":"
            currentMovieID = int(probeLine[0 : len(probeLine) - 1])
            #print (probeLine)
        else :
            currentUserID = int(probeLine)
            estimate = netflix_estimate_rating(currentUserID, currentMovieID, userRatingCache, movieRatingCache)
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
    overallAverage = 3.7
    return overallAverage + (userRatingCache[currentUserID] - overallAverage) + (movieRatingCache[currentMovieID] - overallAverage)
