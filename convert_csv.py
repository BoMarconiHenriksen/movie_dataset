import pandas as pd

# Der er fint at ændre det her til noget andet.
def convert_csv_to_dataframe(file_name):
    data = pd.read_csv(file_name, low_memory=False,  # dtype={"CallGuid": np.int64},
                       usecols=[0, 2, 3, 7, 8, 10, 14, 15, 16], delimiter=',')  # , na_values=['no info', '.']
    return data
    