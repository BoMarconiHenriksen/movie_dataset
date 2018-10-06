
def find_number_of_animated_movies(data):

    # Boolean selection
    count = data[data['genres'].str.contains('Animation')]
    return ("There are " + str(len(count)) + " listed as animation movies.")
