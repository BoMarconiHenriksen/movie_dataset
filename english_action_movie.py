import pandas as pd


def english_action_movie_with_biggest_revenue(data):
    """ data = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                       usecols=[0, 2, 3, 7, 8, 10, 14, 15, ], delimiter=',')  # , na_values=['no info', '.'] """

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # print(data.columns) # ['adult', 'budget', 'genres', 'original_language', 'original_title', 'popularity', 'release_date', 'revenue']

    # Englis action movies
    english_movies = data[data['original_language'] == 'en']
    # print(english_movies)

    # Find action movies
    action_movies_boolean = english_movies['genres'].str.contains('Action')

    # Select the true values and put it in a new list
    action_movies = english_movies[action_movies_boolean].copy()
    # print(action_movies['genres'][45354])

    # Convert string to int
    action_movies['revenue'] = pd.to_numeric(action_movies['revenue'], errors='coerce').copy()

    index_number_biggest_revenue = action_movies['revenue'].idxmax()
    # print(index_number_biggest_revenue)

    # Find the revenue
    biggest_revenue = action_movies['revenue'][index_number_biggest_revenue]
    # print(biggest_revenue)

    # Find the title
    title_biggest_action_revenue = action_movies['original_title'][index_number_biggest_revenue]
    print(title_biggest_action_revenue)
