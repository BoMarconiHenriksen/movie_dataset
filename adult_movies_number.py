
import numpy as np
import pandas as pd


def find_most_popular_adult_movie(data):
   
    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)
    
    # Returns a boolean series
    #filter_true_values = data['adult'] == 'True'
    #print(len(filter_true_values))
    
    filter_true_values = data['adult'] == 'True'

    my_films = data[data['adult'] == 'True']
  

    print("**************************************************************")
    #['adult' 'budget' 'genres' 'original_language' 'original_title'
    # 'popularity' 'release_date' 'revenue' 'runtime']

    fewcol = my_films.loc[:, ["original_title", "release_date", "popularity"]]
    
    #df.plot(kind='scatter',x='num_children',y='num_pets',color='red')

    #print(fewcol[1])
    print(fewcol.columns)
    

    # scatter requires x column to be numeric
    #fewcol.plot(kind='scatter',x='release_date',y='popularity',color='red')
    print(2+2)




    # end 