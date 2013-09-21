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
    fileName is the path to probe.txt
    """    
    lines = [line.strip() for line in fileObject]
    fileObject.close()
    return lines

# -----------------------
# netflix_estimate_rating
# -----------------------

def netflix_estimate_rating (lines, userRatingCache, movieRatingCache) :
    
    currentMovieID = 0
    for line in lines :
        if(line[len(line) - 1] == ":") :
            currentMovieID = int(line[0 : len(line) - 1])
        else :
            currentUserID = int(line)
            netflix_solve(currentMovieID, currentUserID, userRatingCache, movieRatingCache)

# ------------------
# netflix_cache_read
# ------------------

def netflix_cache_read (currentUserID, currentMovieID, userRatingCache, movieRatingCache) :
    averageUserRating = userRatingCache[currentUserID]
    averageMovieRating = movieRatingCache[currentMovieID]
    #if a rating is not found in the cache, guess 2.5 stars
    if(averageUserRating < 1):
        averageUserRating = 2.5
    if(averageMovieRating < 1):
        averageMovieRating = 2.5
    return (averageUserRating + averageMovieRating) / 2.0
