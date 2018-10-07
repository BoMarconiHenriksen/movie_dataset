import pandas as pd
import matplotlib.pyplot as plt


def create_plot_realise_and_runtime(data):

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)
    
    # Runtime sorted
    runtime_sorted = data.sort_values('runtime')
    
    #print(runtime_sorted['runtime'])
