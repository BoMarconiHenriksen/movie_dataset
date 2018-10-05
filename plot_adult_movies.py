import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plotting_adult_and_non_adult_movies(data):
        
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
