import pandas as pd
import numpy as np

# Der er fint at ændre det her til noget andet.
# Fordelen er at det returneres som en dataframe. Vi skal plotte fra enten en dataframe eller series.


def convert_csv_to_dataframe(file_name):
    data = pd.read_csv(file_name, sep=',',na_values=['no info', '.'], dtype={"budget": np.int64},  # dtype={"CallGuid": np.int64}, low_memory=False,
                       usecols=[0, 2, 3, 7, 8, 9, 10, 14, 15, 16])  # squeeze=True.dropna()  # , na_values=['no info', '.']
    return data

# parse_dates=[14], infer_datetime_format=True,


def reader(data):
    print(data.info())
