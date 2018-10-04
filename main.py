""" 
The url to run this program:  https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv
"""
import downloader
import sys
import os

if __name__ == '__main__':
    file_name = downloader.download_file()
