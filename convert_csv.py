import pandas as pd

# Returneres som en dataframe. 
# low_memory=False because column 10 has mixed datatypes.
def convert_csv_to_dataframe(file_name):
    data = pd.read_csv(file_name, sep=',', usecols=[0, 2, 3, 7, 8, 9, 10, 14, 15, 16], low_memory=False) 
    
    # Convert string to int. to_numeric converts to float. fillna sets empty values to 0.
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    data['budget'] = pd.to_numeric(data['budget'], errors='coerce').fillna(0).astype(int)
    data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').fillna(0).astype(int)
    data['runtime'] = pd.to_numeric(data['runtime'], errors='coerce').fillna(0).astype(int)

    # Convert string to int and replace .
    data['popularity'] = pd.to_numeric(data['popularity'].str.replace(
        '.', ''), errors='coerce').fillna(0).astype(int)

    return data
