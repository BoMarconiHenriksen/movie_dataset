""" 
The url to run this program use this url:  https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv
"""
import sys
import os
import downloader
import convert_csv
import lib.most_popular_danish_movie as popular_danish_movie
import lib.english_action_movie as english_action_movie
import lib.plot_reliase_and_runtime as reliase_and_runtime
import lib.plot_adult_movies as plot_adult_movies
import lib.buzz_words as buzz_words


if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file()

data = convert_csv.convert_csv_to_dataframe(file_name)

print(plot_adult_movies.plotting_adult_and_non_adult_movies(data)) # With plot
# ANIMATED MOVIES MANGLER!!!
# MOVIE WITH HIGEST BUDGET MANGLER !!!

#popular_danish_movie.find_most_popular_danish_movie(data)
# !!! print(english_action_movie.english_action_movie_with_biggest_revenue(data))

# Plots
#reliase_and_runtime.create_plot_realise_and_runtime(data)
#buzz_words.find_buzz_words(data)
