import pandas as pd
import matplotlib.pyplot as plt


def create_plot_realise_and_runtime(data):
    """ data = pd.read_csv('movies_metadata.csv', low_memory=False,  # dtype={"CallGuid": np.int64},
                       usecols=[14, 16], delimiter=',') """  # , na_values=['no info', '.']

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    # ['release_date', 'runtime']
    # print(data.columns)

    # Tjek at det er en data frame.
    # print(data.info())
    # print(type(data))

    # Convert strings to Date for adult movies
    data['release_date'] = pd.to_datetime(
        data['release_date'], errors='coerce')

    # print(type(data['release_date']))
    # print(data.info())
    # print(data)

    # Convert strings to int
    data['runtime'] = pd.to_numeric(data['runtime'], errors='coerce')
    # print(type(data['runtime']))

    # x = data['release_date'].sort_values()
    # print(x)
