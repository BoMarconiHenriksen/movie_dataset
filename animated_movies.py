import numpy
import load_data
from ast import literal_eval
import pandas as pd
import io
import requests
#https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options

def animated_movies():

    url = 'https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv'
    #s=requests.get(url).content
    #c=pd.read_csv(io.StringIO(s.decode('utf-8')))
    #data=pd.read_csv(url)
    #print(data.columns)
    data = pd.read_csv('movies_metadata.csv', dtype={'a': np.float}) 
    print(data.columns)
    print(data.dtypes)


# end
'''
['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id',
       'imdb_id', 'original_language', 'original_title', 'overview',
       'popularity', 'poster_path', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime',
       'spoken_languages', 'status', 'tagline', 'title', 'video',
       'vote_average', 'vote_count']
'''

'''
import pandas as pd
import io
import requests
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
'''



'''

    data = pd.read_csv("movies_metadata.csv", dtype=str)#, low_memory=False) 
#print(data.dtypes)
#print(data.columns)

animated = load_data.load_movie_data('movies_metadata.csv', {}, {})
    animated = pd.read_csv('movies_metadata.csv', sep=',')
    #print(animated[100][0])
    #print(animated[100][1])
    #print(animated[100][2])
    #print(animated[100][3])  # list of json
    #print(animated[0])
    

    mytype = animated[100][3]
    print(len(mytype)) # 88 listen er gemt som en string med længde 88
    #type2 = pd.eval(mytype)#literal_eval(mytype)
    print(type2)
    print(len(type2))
    print(type(type2))
'''