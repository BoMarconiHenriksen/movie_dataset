import load_data
import csv_reader

import json
from pprint import pprint

""" with open('data.json') as f:
    data = json.load(f)

pprint(data) """

# Json blob til json_fil.tooString. Returner dictinary.


def adult_movies():
    #data_of_movies = csv_reader.load_data('movies_metadata.csv')
    adult = load_data.load_movie_data('movies_metadata.csv', {'True': 0}, {})

    print(len(adult))

    for movie in adult:
        print(movie[8])

    adultdict = {}
    for movie in data_of_movies:
        adultdict.setdefault(movie[0], 0)
        adultdict[movie[0]] += 1
    print(data_of_movies[1][0])

    # print(adultdict)
    # print(adult[0])
    # print(data_of_movies[1])
    # print(len(data_of_movies))
