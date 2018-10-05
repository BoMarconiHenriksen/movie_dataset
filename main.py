""" 
The url to run this program:  https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv
"""
import sys
import os
import downloader
import convert_csv
import most_popular_danish_movie
import english_action_movie
import plot_reliase_and_runtime
import plot_adult_movies
import adult_movies_number

if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file()

data = convert_csv.convert_csv_to_dataframe(file_name)
#english_action_movie.english_action_movie_with_biggest_revenue(data)
#plot_adult_movies.plotting_adult_and_non_adult_movies(data)
#most_popular_danish_movie.find_most_popular_danish_movie(data)
#plot_reliase_and_runtime.create_plot_realise_and_runtime(data)

adult_movies_number.find_most_popular_adult_movie(data)