# ------------------
# netflix_make_cache
# ------------------

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

# ------------------
# netflix_read_probe
# ------------------

def netflix_read_probe (fileObject) :
    """
    fileObject is for the probe input
    """    
    lines = [line.strip() for line in fileObject]
    fileObject.close()
    return lines

# -------------------
# netflix_read_actual
# -------------------

def netflix_read_actual (fileObject) :
    """
    fileObject is for the actual scores
    acutalRatings is a list of dictionaries
    """
    actualRatings = [None] * 17771
    userMap = {}
    currentMovieID = 0
    for line in fileObject :
        line = line.strip()
        if (line[len(line) - 1] == ":") :
            actualRatings[currentMovieID] = userMap
            userMap = {}
            currentMovieID = int(line[0 : len(line) - 1])
        else :
            (userID, rating) = line.split()
            userMap[int(userID)] = float(rating)
    actualRatings[currentMovieID] = userMap
    fileObject.close()
    return actualRatings

# -----------------------
# netflix_estimate_rating
# -----------------------

def netflix_compute_RMSE (probeLines, actualRatings, userRatingCache, movieRatingCache) :
    """
    summation of the difference between our estimate and the actual ratings
    writes our estimates to output file
    """
    currentMovieID = 0
    sumRMSE = 0.0
    totalRatings = 0
    for probeLine in probeLines :
        #if line containing a movie ID number
        if (probeLine[len(probeLine) - 1] == ":") :
            currentMovieID = int(probeLine[0 : len(probeLine) - 1])
            print (probeLine)
        else :
            currentUserID = int(probeLine)
            estimate = netflix_estimate_rating(currentUserID, currentMovieID, userRatingCache, movieRatingCache)
            assert estimate >= 1.0 and estimate <= 5.0
            sumRMSE += (estimate - actualRatings[currentMovieID][currentUserID]) ** 2
            totalRatings += 1
            print (str(estimate))
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
