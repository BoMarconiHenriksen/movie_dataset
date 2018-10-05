from collections import Counter
import pandas as pd
from collections import defaultdict
from collections import Counter


    #print(data.columns.values)

    # ['adult' 'budget' 'genres' 'original_language' 'original_title' 'overview'
    # 'popularity' 'release_date' 'revenue' 'runtime']
    # false_values_count_dates = false_values.groupby('release_date').size()

    # create list of all words from all "overview" columns.


# tager en string og en liste af ord (fra get_buzz100), of finder alle forekomster af ordene i strengen
def buzz_count(overview_string, buzz_list):
    d = defaultdict(int)
    for word in overview_string.split():
        if word in buzz_list:
            d[word] += 1
    return sum(d.values()) 

# returnere de 100 mest brugte ord i "overview" kolonnen
def get_buzz100(data):
    test1 = data["overview"].astype(str)
    test2string = ' '.join(test1)
    word_dict = defaultdict(int)
    for word in test2string.split():
        word_dict[word] += 1
    mycount = Counter(word_dict).most_common(100)
    buzz_list = []
    buzz_list = [k[0] for k in mycount]
    return buzz_list

def find_buzz_words(data):

    buzz_list = get_buzz100(data)

    # data["overview"] = buzz_count(data["overview"], buzz_list)

    #print(data)
    #print(data.loc[0, "original_language"])
    # https://stackoverflow.com/questions/12604909/pandas-how-to-change-all-the-values-of-a-column
    # df['Date'].str[-4:].astype(int)


    # hvordan erstatter jeg "overview" strengen i data med tallet fra buzz_count
    # (jeg vil erstatte kolonne værdier i stedet for at lave en ny kolonne 
    # for at være sikker på at de rigtige buzz_count værdier associeres med den rigtige kolonne)
    #data["overview"]



    #     df2.loc["Alaska":"Arkansas","2005":"2007"]
    #w['female'] = w['female'].map({'female': 1, 'male': 0})







    # end
