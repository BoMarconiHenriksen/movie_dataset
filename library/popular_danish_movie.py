import pandas as pd


def find_most_popular_danish_movie(data):

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # Find all the danish movies.
    danish_movies = data[data['original_language'] == 'da'].copy()

    # Find the index number of the highest int in popularity.
    index_number_most_popular = danish_movies['popularity'].idxmax()
    
    most_popular_rating = danish_movies['popularity'][index_number_most_popular]
    most_popular_title = danish_movies['original_title'][index_number_most_popular]

    return("The most popular danish movie is: " + most_popular_title + ". The rating is: " + str(most_popular_rating) + ".")
