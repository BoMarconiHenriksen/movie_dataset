import load_data
import pandas as pd

def highest_movie_budget():
    budget = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                           usecols=[2, 8], delimiter=',', na_values=['no info', '.'])
    
    pd.set_option('display.max_columns', None)

    #budget_movies = budget[budget['budget']] 
    budget_movies = budget[budget.columns[0]]

    budget_movies['budget'] = pd.to_numeric(budget_movies['budget'], errors='coerce')

    index_highest_budget = budget_movies['budget'].idxmax()

    highest_budget = budget_movies['budget'][index_highest_budget]




    #print(budget)

    #max_budget = budget[budget.columns[0]]
    
    #max_budget = list(map(int, max_budget))

    #print(max(list(max_budget)))
    #print(max(list_budget))
    print(highest_budget)