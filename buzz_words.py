import pandas as pd
import matplotlib.pyplot as plt


def find_buzz_words(data):
    # Joins the words to 1 string, then split and count the values. Return a series.
    #word_count = pd.Series(' '.join(data['overview'].astype(str)).split()).value_counts()
    #most_used_words = word_count[:100]
    #print(most_used_words)

    # Convert string to int. to_numeric converts to float. fillna sets empty values to 0.
    data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').fillna(0).astype(int).copy()
    #print(data['revenue'])

    # Sort revenue column.
    revenue_sorted = data.sort_values('revenue')
    # print(revenue_sorted['revenue'])

    # Convert string to int for budget.
    data['budget'] = pd.to_numeric(data['budget'], errors='coerce').fillna(0).astype(int).copy()
    # print(data['budget'])

    # Budget sorted
    revenue_sorted = data.sort_values('budget')
    print(revenue_sorted['budget'])

    #plt.plot( 'x', 'y', data=df, linestyle='none', marker='o')
    

    """ df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                    [6.4, 3.2, 1], [5.9, 3.0, 2]],
                   columns=['length', 'width', 'species']) """
    """ ax1 = df.plot.scatter(  x='length',
                            y='width',
                            c='DarkBlue') """
    #plt.show()

