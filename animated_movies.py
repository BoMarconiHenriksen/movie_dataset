import pandas as pd
import numpy as np
import load_data


def animated_movies():
    #animated = load_data.load_movie_data('movies_metadata.csv', {}, {})
    """ 
    print(animated[100][0])
    print(animated[100][1])
    print(animated[100][2])
    print(animated[100][3]) """
    animated = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                           usecols=[2, 3, 4], delimiter=',', na_values=['no info', '.'])

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # print(animated)
    # print(animated.head().to_string())
    # print animated.describe().to_string()
    print(animated.tail())
    # print(animated.sample(3))
    # Select specific columns of your dataframe
    # print(animated([]))
    # print(animated['genres'])
    # print(animated['genres'][45463])
    #print(animated[['genres', 'budget']])
