# ------------
# netflix_make_cache
# ------------

def netflix_make_cache (cache, fileName) :
    """
    
    """    
    fileObject = open(fileName)
    num = 0
    for line in fileObject: 
        line = line.strip()
        (i, j) = line.split(" ")
        cache[int(i)] = float(j)

# ------------
# netflix_read
# ------------

def netflix_read (fileName) :
    """
    fileName is the path to probe.txt
    """    
    fileObject = open(fileName)
    lines = [line.strip() for line in fileObject]
    fileObject.close()
    return lines

# -------------
# netflix_parse
# -------------

def netflix_parse (lines, userRatingCache, movieRatingCache) :
    currentMovieID = 0
    for line in lines :
        if(line[len(line) - 1] == ":") :
            currentMovieID = int(line[0 : len(line) - 1])
        else :
            currentUserID = int(line)
            netflix_solve(currentMovieID, currentUserID, userRatingCache, movieRatingCache)

# -------------
# netflix_solve
# -------------

def netflix_solve (currentMovieID, currentUserID, userRatingCache, movieRatingCache) :
    1 + 1
