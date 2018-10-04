import pandas as pd


def find_most_popular_danish_movie():
    data = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                       usecols=[0, 2, 3, 7, 8, 10, 14, 15, ], delimiter=',')  # , na_values=['no info', '.']

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # print(data.columns)

    # We are going to work with columns 'original_language', 'popularity'
    danish_movies = data[data['original_language'] == 'da']
    #danish_movies.popularity = pd.to_numeric('popularity', errors='coerce').fillna(0).astype(np.int64)

    # Convert string to int
    danish_movies['popularity'] = pd.to_numeric(
        danish_movies['popularity'], errors='coerce')

    # Find the index number of max int
    index_number_most_popular = danish_movies['popularity'].idxmax()

    # Find the popularity number
    most_popular_number = danish_movies['popularity'][index_number_most_popular]

    # Find the title
    most_popular_title = danish_movies['original_title'][index_number_most_popular]
    print(most_popular_title)
