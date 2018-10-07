""" 
The url to run this program use this url:  https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv
"""
import downloader
import convert_csv
import library.popular_danish_movie as popular_danish_movie
import library.english_action_movie as english_action_movie
import library.plot_reliase_and_runtime as reliase_and_runtime
import library.plot_adult_movies as plot_adult_movies
import library.buzz_words as buzz_words
import library.animated_movies as animated_movies
import library.highest_budget as highest_budget

if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file()

data = convert_csv.convert_csv_to_dataframe(file_name)

#convert_csv.reader(data)


print(plot_adult_movies.plotting_adult_and_non_adult_movies(data)) # With plot
print(animated_movies.find_number_of_animated_movies(data))
print(highest_budget.find_highest_budget(data))
print(popular_danish_movie.find_most_popular_danish_movie(data))
print(english_action_movie.english_action_movie_with_biggest_revenue(data))

# Plots - Der er lavet dataframes men plot mangler.
reliase_and_runtime.create_plot_realise_and_runtime(data)
buzz_words.find_buzz_words(data)
