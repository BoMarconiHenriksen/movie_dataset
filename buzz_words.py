from collections import Counter
import pandas as pd
from collections import defaultdict
from collections import Counter


def find_buzz_words(data):
    # Joins the words to 1 string, then split and count the values. Return a series.
    word_count = pd.Series(' '.join(data['overview'].astype(str)).split()).value_counts()
    most_used_words = word_count[:100]
    print(most_used_words)


    #  Det virker til at denne her metode tager længere tid end join metoden.
    # Expand the splitted strings into separate columns. Multidimentionally.
    # Stack the prescribed level(s) from columns to index.
    # value_counts: Returns object containing counts of unique values.
    #d = data['overview'].str.split(expand=True).stack().value_counts()
    # print(d)
