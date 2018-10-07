
def find_number_of_animated_movies(data):
    ''' 
    The method finds the number of animation movies in the genres column in the movie dataset.
    '''

    # Boolean selection
    count = data[data['genres'].str.contains('Animation')]

    return ("There are " + str(len(count)) + " listed as animation movies.")
