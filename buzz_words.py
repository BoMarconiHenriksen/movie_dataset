import pandas as pd
import matplotlib.pyplot as plt


def find_buzz_words(data):
    # Joins the words to 1 string, then split and count the values. Return a series.
    word_count = pd.Series(' '.join(data['overview'].astype(str)).split()).value_counts()
    most_used_words = word_count[:100]
    
    # Convert string to int. to_numeric converts to float. fillna sets empty values to 0.
    data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').fillna(0).astype(int).copy()
    
    # Sort revenue column.
    revenue_sorted = data.sort_values('revenue')
    
    # Convert string to int for budget.
    data['budget'] = pd.to_numeric(data['budget'], errors='coerce').fillna(0).astype(int).copy()
   
    # Budget sorted
    budget_sorted = data.sort_values('budget')
    
    #ax = revenue_sorted.plot(kind='scatter', x = 'revenue', y=budget_sorted['budget'])
    
    


    #plt.show()

