import load_data

def animated_movies():
    animated = load_data.load_movie_data('movies_metadata.csv', {'Animation': 3}, {})
    print(len(animated))