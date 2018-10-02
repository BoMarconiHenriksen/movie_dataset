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

    #print(sys.argv)
    #study_in_scarlet_url = 'https://www.gutenberg.org/files/244/244-0.txt'
    #file_name = 'study_in_scarlet.txt'
    #download(study_in_scarlet_url, file_name)
    print(sys.argv)
    befolkningkbh_url= 'https://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
    file_name = 'befolkningkbh.txt'
    download(befolkningkbh_url,file_name)
    