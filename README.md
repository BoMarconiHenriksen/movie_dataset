# Movie Dataset from Plain Product

## Documentation
Analyzine the movie dataset from the group Plain Product. This is the link to the assignment https://github.com/MikkelHansen95/dataset/blob/master/README.md  

## Group
Anders Nissen, Christian Lykke and Bo Henriksen.  

## How to run the project
1. Clone the project  
2. Cd into the directory of the project  
3. To run the project you need to paste this url to the dataset as a parameter https://raw.githubusercontent.com/MikkelHansen95/dataset/master/movies_metadata.csv  

4. Example of how to run the project  
5. python main.py [<url_to_dataset>]  

## Dependencies
The project does only use dependencies which is part of Pythons Anaconda installation.  

## Results
- [x] How many movie are rated adult?  
Number of movies reated as adult is: 9  

- [x] How many movies are listed as animation?  
There are 1935 listed as animation movies.  

- [x] Which movie had the highest budget?  
The name of the movie with the highest budget is: Pirates of the Caribbean: On Stranger Tides .The budget was 380000000.  

- [x] Which danish movie is most popular?  
The most popular danish movie is: Fasandræberne. The rating is: 12635996.  

- [x] Which english action movie had the biggest revenue?  
The english action movie with the biggest revenue is: Star Wars: The Force Awakens. The revenue was: 2068223624.  

- [x] Plot histogram with number of movies according to release day for 'adult' and 'non adult' movies.   
Plot via 2 series objects.  
x-axis: release date (day/month)  
y-axis: number of movies   

![alt text](https://github.com/BoMarconiHenriksen/movie_dataset/blob/developer/movies_per_year.png)  

- [ ] Scatter-Plot with runtime as y value and release date as x value.  
Vi mangler kun plottet!  
Plot via dataframe.  
x-axis: runtime  
y-axis: relase date (day/month)  

- [ ] 3D Scatter-Plot with the word frequency for each movie out of the 100 most used 'buzzwords' from all movies overviews (Firstly find 100 most used 'buzzwords' and then find the frequency of these words in each movies overview)  
Mangler kun plottet!  
x-axis: revenue  
y-axis: budget  
z-axis: buzzword count   

