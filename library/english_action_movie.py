import pandas as pd


def english_action_movie_with_biggest_revenue(data):

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # Find all the english movies
    english_movies = data[data['original_language'] == 'en']

    # Find action movies
    action_movies_boolean = english_movies['genres'].str.contains('Action')

    # Select the true values and put it in a new list
    action_movies = english_movies[action_movies_boolean].copy()

    index_number_biggest_revenue = action_movies['revenue'].idxmax()

    biggest_revenue = action_movies['revenue'][index_number_biggest_revenue]
    title_biggest_action_revenue = action_movies['original_title'][index_number_biggest_revenue]

    return ("The english action movie with the biggest revenue is: " + title_biggest_action_revenue + ". The revenue was: " + str(biggest_revenue) + ".")
