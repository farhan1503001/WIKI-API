import ssl
import requests
from bs4 import BeautifulSoup
import difflib
import pandas as pd
import csv
import sqlite3
#Preparing context for handeling SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
#Opening the header files selected in initial phase
with open('header_col.csv') as filer:
    reader=csv.reader(filer)
    headers=list()
    for item in reader:
        headers.append(item)

headers=headers[0]
print(headers)
#Manually inputting url and saving 'base' for future use.
url='https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
base='https://en.wikipedia.org'
page=requests.get(url=url)
soup=BeautifulSoup(page.content,'html.parser')

#Finding the number of rows in movie column
number_of_rows = len(soup.find_all('tr'))
print(number_of_rows)

#checker function
#This function inserts comma between names of different persons where for some instance that was missing
def lowupfind(word):
    Length=len(word)
    for i in range(Length-1):
        if i==0:
            continue
        if word[i].islower() and word[i+1].isupper():
            word=word[:i+1]+', '+word[i+1:]
    return word


#Data Extraction phase
#Selecting the first movie(Nomadland) as reference
import time
movie_dataset=list()
for line in range(number_of_rows):
    '''
    if line==50:
        break
    '''
    data={}
    header='https://en.wikipedia.org'
    try:
        movie_list=soup.find_all('i')[line].find('a')
        if movie_list is None:   #This is called only for extra useless <i> tag
            raise Exception(line)
    except Exception as e:
        print(e)
        continue
    data['Name']=movie_list.text #Assigning movie names
    response=requests.get(header+movie_list['href'])
    item_movie=BeautifulSoup(response.content,'html.parser')
    row_table=item_movie.find_all('tr')
        #Find director
    for value in row_table:
        try:
            lb=value.find_all('th',{'class':'infobox-label'})[0]
            match_find=difflib.get_close_matches(lb.text,headers,cutoff=0.8) #Matching header name with the coloumn data we want
            if len(match_find)>0:
                matched_col=match_find[0]
                info=value.find_all('td',{'class':'infobox-data'})[0] #Finding all data under the header
                
                temp=info.text.split('[')[0]
                #data[matched_col]=temp
                #'''
                temp=temp.replace('\xa0',' ')#Some date has got these unicode tags removing that.
                temp=lowupfind(temp)
                if temp[0]=='\n' and temp[-1]=='\n': #For removing all new line unnecessarily put.
                    data[matched_col]=temp[1:-1].replace('\n',', ')
                elif temp[0]=='\n' and temp[-1]!='\n':
                    data[matched_col]=temp[1:].replace('\n',', ')
                else:
                    data[matched_col]=temp
                #'''
                #print('--------')
                #data[matched_col]
                #print(lb.text,matched_col)
                #time.sleep(1)
            else:
                pass
           
        except:
            pass
    movie_dataset.append(data)#Appending each dictionary to the list
#Converting extracted data to pandas dataframe
movie_data_frame=pd.DataFrame(movie_dataset) #Converting to pandas dataframe for clear observation
#movie_data_frame[0:50]
#Reading extra information from csv file could have also used url instead of file
genre_set= pd.read_csv('movies.csv')
rating_set=pd.read_csv('ratings.csv')
#Firststart working with genre
#Differentiating year from name of under title column
name=genre_set['title'].str.split('(')
genre_set['name']=[value[0][:-1] for value in name]
#print(genre_set['name'])
temp_val=list()
for temp in name:
    #print(temp[1]) #There are not only single string name but also multiple strings
    temp_val.append(temp[-1][:-1])
#print(temp_val)
genre_set['year']=temp_val
#Now work with ratings csv file
ratings_set=pd.read_csv('ratings.csv')
#ratings_set.head()
#Perform join operation with genre_set for movie name
ratings_genre=genre_set[['movieId','name','year','genres']].merge(ratings_set,on='movieId',how='inner')
#Perform necessary operation for finding usercount and average rating
final_average=ratings_genre.groupby(['movieId','name','year']).aggregate({'userId':'count','rating':'mean'})
#Merging for just adding genre,not fully necessary
final_average_use=final_average.merge(genre_set[['movieId','name','year','genres']],on='movieId',how='inner')
#Adding avg_rating and user count column
count=0
prev_dataset=movie_data_frame
for row in final_average_use.itertuples():
    print(row.name)
    for scrap in prev_dataset.itertuples():
        if scrap.Name==row.name:
            print(scrap.Name,row.name)
            prev_dataset.loc[scrap.index,'Average Rating']=row.rating
            prev_dataset.loc[scrap.index,'User Count']=row.userId
#Adding genres
count=0
#'''
for row1 in genre_set.itertuples():
    #print(row.name)
#'''
#name='Toy Story'
    for scrap1 in prev_dataset.itertuples():
        if scrap1.Name==row1.name:
            print(scrap1.Name,row1.name)
            prev_dataset.loc[scrap1.index,'Genres']=row1.genres
#For removing Nan
new_dataset=prev_dataset.fillna('Not Available')
#Saving to database for using with REST API
new_connection=sqlite3.connect('wikiapi/api_database.sqlite3')
new_dataset.to_sql('movies',new_connection)
new_connection.close()
