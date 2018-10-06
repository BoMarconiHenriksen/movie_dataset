import pandas as pd
import matplotlib.pyplot as plt


def create_plot_realise_and_runtime(data):

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)

    #Convert strings to Date for adult movies
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')

    # Convert strings to int
    data['runtime'] = pd.to_numeric(data['runtime'], errors='coerce').fillna(0).astype(int)
    
    # Runtime sorted
    runtime_sorted = data.sort_values('runtime')
    
    #print(runtime_sorted['runtime'])
