"""
Usage:
    python downloader.py <url> [<file_name>]
"""

import os
import sys
from urllib import request as req

def download(from_url, to_file):
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file )
    
if __name__ == '__main__':
    #if len(sys.argv) >= 2

    try: 
        _, url, file_name = sys.argv
    except: 
        try:
            _, url = sys.argv
            file_name = os.path.basename(url)
        
        except:
            try:
                #open file
                cfg_file = 'list_of_files.txt'
                with open(cfg_file) as fp:
                    for line in fp:
                        file_name = os.path.basename(line.rstrip())
                        url = line
                        download(url, file_name)
                sys.exit(0)

                #fp = open(cfg_file)
                #try:
                #    for line in fp:
                #        print(line)
                #finally:
                #    fp.close()
            #except Exception as e:
            except:
                #raise e
                print(__doc__)
                sys.exit(1)
    download(url, file_name)