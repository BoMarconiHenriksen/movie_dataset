import pandas as pd
import numpy as np
import load_data
import matplotlib.pyplot as plt
# https://towardsdatascience.com/pandas-tips-and-tricks-33bcc8a40bb9


def animated_movies():
    #animated = load_data.load_movie_data('movies_metadata.csv', {}, {})
    """ 
    print(animated[100][0])
    print(animated[100][1])
    print(animated[100][2])
    print(animated[100][3]) """
    animated = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                           usecols=[0, 2, 3, 7, 10, 14, 15, ], delimiter=',')  # , na_values=['no info', '.']

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # print(animated)
    # print(animated.head().to_string())
    # print animated.describe().to_string()
    # print(animated.tail())
    # print(animated.sample(3))
    # Select specific columns of your dataframe
    # print(animated([]))
    # print(animated['genres'])
    # print(animated['genres'][45463])
    # print(animated[['genres', 'budget']])
    # print(animated.columns)  # release_date
    # print(animated.head())

    #data_series = pd.Series(animated[animated.columns[5]])

    # print(animated['release_date'])

    # Put the column with dates in one variable
    dato_series = pd.Series(animated[animated.columns[5]])
    # Count the same days
    counts_the_date = pd.Series.value_counts(dato_series)
    # print(counts_the_date)
    """ counts_the_date['release_date'] = pd.to_datetime(
        counts_the_date['release_date'])

    print(counts_the_date.info()) """

    # * * * * * * *
    # KODEN INDEN FOR STJERNERNE VIRKER

    # Convert strings to Date
    animated['release_date'] = pd.to_datetime(
        animated['release_date'], errors='coerce')
    # print(animated.info())
    # print(animated['release_date'])

    # Count same days. Index is now the date and the count is the value.
    count_dates = animated.groupby('release_date').size()
    # print(type(count_dates))

    plot_file = 'movies_per_year.png'

    plt.figure()
    # count_dates.plot()
    count_dates.hist()
    plt.show()

    ax = count_dates.plot()
    fig = ax.get_figure()

    fig.savefig(plot_file)

# * * * * * * *

# Change release_date column to index. Virker kun på dataframes.
#count_dates.set_index('release_date', inplace=True)
# print(count_dates)

# count_dates.sort_index()
# print(count_dates)


""" animated['release_date'] = pd.Series.value_counts(animated['release_date'])
    print(animated['release_date']) """
#b = animated.groupby(animated["release_date"])

""" b = animated.groupby('release_date').value_counts()

    print(b) """

#a = pd.to_datetime(dato_series, format='%Y-%m-%d')

# print(type(a))
#
# a.index
# print(a)
#sorted_by_date = a.sort_values(by='release_date')
#sorted_by_date = pd.Series.sort_value(a)
# a.sort_values(by=['release_date'])
#a.sort_values('release_date', inplace=True)
# print(a)

# a = counts_the_date.sort_values(counts_the_date)
# print(a)

# Animation
"""     counts = animated['genres'].value_counts()

    print(counts['Animation']) """
