import pandas as pd
import matplotlib.pyplot as plt


def find_buzz_words(data):
    # Joins the words to 1 string, then split and count the values. Return a series.
    word_count = pd.Series(' '.join(data['overview'].astype(str)).split()).value_counts()
    most_used_words = word_count[:100]
    
    # Sort revenue column.
    revenue_sorted = data.sort_values('revenue')
   
    # Budget sorted
    budget_sorted = data.sort_values('budget')
    
    #ax = revenue_sorted.plot(kind='scatter', x = 'revenue', y=budget_sorted['budget'])
    
    


    #plt.show()

