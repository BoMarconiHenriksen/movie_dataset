import downloader
import csv

def load_data(file_name):
    with open(file_name) as fn:
        reader = csv.reader(fn)
        data = list(reader)
        return data
