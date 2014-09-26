netflix-prize
=============
This Python 2.7 software analyzes data from the <a href = "http://www.netflixprize.com/">Netflix Prize</a> challenge that sought to achieve the lowest possible <a href = "http://en.wikipedia.org/wiki/Root_mean_square_error">root mean square error</a>. For this project, my software obtained an RMSE of approximately 0.9 stars for the data provided by Netflix.

The movie rating files contain over 100 million ratings from 480,000 randomly-chosen, anonymous Netflix customers over 17,000 movie titles.  The data was collected between October 1998 and December 2005 and reflect the distribution of all ratings received during this period.  The ratings are on a scale from 1 to 5 (integral) stars. To protect customer privacy, each customer ID has been replaced with a randomly-assigned ID.  The date of each rating and the title and year of release for each movie ID are also provided. The original data can be found <a href = "http://www.cs.utexas.edu/users/downing/netflix/training_set/">here</a>. For the sake of performance and simplicity, I built caches for averages.

To run the code, use the command <code>python RunNetflix.py < RunNetflix.in > RunNetflix.out</code>. To test the code, use the command <code>python TestNetflix.py > TestNetflix.out</code>
