from collections import Counter
import pandas as pd


def find_buzz_words(data):
    # print(data.columns)
    #count_words = data['overview'].str.get_dummies(sep=' ').T.dot(data['overview'])
    # data['word_count'] = data['overview'].apply(Counter(lambda x: x.lower().split()))
    #result = data['overview'].apply(pd.value_counts)
    # print(pd.value_counts(data['overview'].values))
    # print(data.info())
    #seperated_words = data['overview'].str.get_dummies(sep=' ')
    # print(seperated_words)
    # print(data['overview'].str.get_dummies(sep=' ').value_counts())

    # dropping null value columns to avoid errors
    #data.dropna(inplace = True)
    data['split_words'] = data['overview'].str.split(' ')
    # print(type(data))
    # print(data.columns)
    dates = data.groupby('split_words').size()
    print(dates)
    #counts = data['split_words'].value_counts()#.to_dict()
    #print(counts)
    # print(data['split_words'])
    #count = data['split_words'].value_counts()

    #data['count_words'] = data['split_words'].str(Counter())
    # print(data['count_words'])
