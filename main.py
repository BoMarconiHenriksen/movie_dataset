""" 
The url to run this program:  https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv
"""
import sys
import os
import downloader
import convert_csv

if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file()

data = convert_csv.convert_csv_to_dataframe(file_name)
