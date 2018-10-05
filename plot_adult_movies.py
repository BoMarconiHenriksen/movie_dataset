import pandas as pd
import numpy as np
import load_data
import matplotlib.pyplot as plt
# https://towardsdatascience.com/pandas-tips-and-tricks-33bcc8a40bb9
# https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-39e811c81a0c


def plotting_adult_and_non_adult_movies(data):
    #animated = load_data.load_movie_data('movies_metadata.csv', {}, {})
    """ 
    print(animated[100][0])
    print(animated[100][1])
    print(animated[100][2])
    print(animated[100][3]) """
    """ animated = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                           usecols=[0, 2, 3, 7, 10, 14, 15, ], delimiter=',') """  # , na_values=['no info', '.']

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
    #dato_series = pd.Series(data[data.columns[5]])
    # Count the same days
    #counts_the_date = pd.Series.value_counts(dato_series)
    # print(counts_the_date)
    """ counts_the_date['release_date'] = pd.to_datetime(
        counts_the_date['release_date'])

    print(counts_the_date.info()) """

    # * * * * * * *
    # KODEN INDEN FOR STJERNERNE VIRKER

    # Boolean selection
    # Returns a boolean series
    filter_true_values = data['adult'] == 'True'
    # print(filter_true_values)

    # Select the true values and put it in a new list
    true_values = data[filter_true_values].copy()
    # print(len(true_values))

    # The same as above in a one liner
    #true_values = animated[animated['adult'] == 'True']
    # print(len(true_values))
    # print(true_values)

    false_values = data[data['adult'] == 'False'].copy()
    # print(len(false_values))
    # print(false_values)

    # Convert strings to Date for adult movies
    true_values.loc['release_date'] = pd.to_datetime(true_values['release_date'], errors='coerce').copy()
    # print(true_values.info())
    # print(true_values['release_date'])

    # Convert strings to Date for non-adult movies
    false_values.loc['release_date'] = pd.to_datetime(false_values['release_date'], errors='coerce').copy()
    # print(false_values.info())
    # print(false_values['release_date'])

    # Count same days. Index is now the date and the count is the value.
    # Der er en adult movie uden data, derfor ryger vi ned på 8 adult movies.
    true_values_count_dates = true_values.groupby('release_date').size()
    # print(type(true_values_count_dates))
    # print(len(true_values_count_dates))
    # print(true_values_count_dates)

    false_values_count_dates = false_values.groupby('release_date').size()
    #print(false_values_count_dates)

    # plot_file = 'movies_per_year.png'

    # plt.figure()

    # plt.figure()
    # true_values_count_dates.plot()

    #plt.plot(true_values_count_dates, marker='o', linestyle='--', color='r', label='Adult movies')
    #plt.plot(false_values_count_dates, marker='*', linestyle='--', color='g', label='Non-adult movies')

    # plt.show()

    #ax = count_dates.plot()
    #fig = ax.get_figure()

    # fig.savefig(plot_file)

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
