import pandas as pd

def find_highest_budget(data):

    index_number_highest_budget = data['budget'].idxmax()
    
    # Find the revenue and title of the movie with highest budget.
    highest_budget = data['budget'][index_number_highest_budget]
    name_of_movie = data['original_title'][index_number_highest_budget]

    return ("The name of the movie with the highest budget is: " + name_of_movie + " .The budget was " + str(highest_budget) + ".")

