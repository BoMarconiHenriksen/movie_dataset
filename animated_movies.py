import load_data


def animated_movies():
    animated = load_data.load_movie_data('movies_metadata.csv', {}, {})
    print(animated[100][0])
    print(animated[100][1])
    print(animated[100][2])
    print(animated[100][3])
