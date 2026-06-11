 # using movie_index find similarity array from similarity_matrix
    # use enumerate to have : index_of_movie, similarity_values
    # convert to list
    # use sorted(reverse = True, lambda x : x[1])
    # becoz of enumerate 2 values are present for each movie in list. 1st is index, 2nd is similarity value. 
    # we need to order the movies on the basis of similarity value. use lambda x : x[1], which tells to not choose index and choose similarity value
    # revserse = True -> orders the values from highest to lowest
    # take only 5 movie name: slice method -> [1:6]
