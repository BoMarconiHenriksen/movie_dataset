import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def plotting_adult_and_non_adult_movies(data):
    '''
    This method find the number of adult movies in the dataset 
    and plot both adult movies and non-adult movies.
    '''
    # Boolean selection. Returns a boolean series
    filter_true_values = data['adult'] == 'True'
   
    # Select the true values and put it in a new list
    adult_movies = data[filter_true_values].copy()
    number_of_adult_movies = (len(adult_movies))

    # The same as above in a one liner for non adult movies.
    non_adult_movies = data[data['adult'] == 'False'].copy()

    # Count same days. Index is now the date and the count is the value.
    # Der er en adult movie uden date, derfor ryger vi ned på 8 adult movies.
    adult_movies_count_dates = adult_movies.groupby('release_date').size()
    non_adult_movies_count_dates = non_adult_movies.groupby('release_date').size()
    
    plot_file = 'movies_per_year.png'

    data_to_be_plotted = pd.concat([non_adult_movies_count_dates, adult_movies_count_dates], sort=True, axis=1, keys=['Non Adult Movies','Adult Movies'])
    data_to_be_plotted.plot()
        
    # For tests.
    # plt.show()
    
    ax = data_to_be_plotted.plot()
    ax.set_title('Adult and Non Adult Movies')
    ax.legend(loc='upper center')
    ax.set_ylabel('Number of Movies')
    ax.grid(False) # Get som space just below 0 on x axe.
    
    fig = ax.get_figure()

    fig.savefig(plot_file)

    return ("Number of movies reated as adult is: " + str(number_of_adult_movies))
