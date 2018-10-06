import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def plotting_adult_and_non_adult_movies(data):

    # Boolean selection. Returns a boolean series
    filter_true_values = data['adult'] == 'True'
   
    # Select the true values and put it in a new list
    adult_movies = data[filter_true_values].copy()
    number_of_adult_movies = (len(adult_movies))

    # The same as above in a one liner for non adult movies.
    non_adult_movies = data[data['adult'] == 'False'].copy()

    # Convert strings to Date for adult movies
    adult_movies.loc['release_date'] = pd.to_datetime(adult_movies['release_date'], errors='coerce').copy()

    # Convert strings to Date for non-adult movies
    non_adult_movies.loc['release_date'] = pd.to_datetime(
        non_adult_movies['release_date'], errors='coerce').copy()

    # Count same days. Index is now the date and the count is the value.
    # Der er en adult movie uden data, derfor ryger vi ned på 8 adult movies.
    adult_movies_count_dates = adult_movies.groupby('release_date').size()
    non_adult_movies_count_dates = non_adult_movies.groupby('release_date').size()
    
    plot_file = 'movies_per_year.png'

    non_adult_movies_count_dates.plot()

    # plt.show()

    ax = non_adult_movies_count_dates.plot()
    fig = ax.get_figure()

    fig.savefig(plot_file)

    return ("Number of movies reated as adult is: " + str(number_of_adult_movies))
