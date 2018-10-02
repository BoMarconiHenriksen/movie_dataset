import downloader
import sys

if __name__ == '__main__':
    _, url = sys.argv
    _, url, file_name = sys.argv

file_name = downloader.download(url, to_file)