import newspaper
import os
import pandas as pd
from collections import Counter
from requests_html import HTMLSession


os.chdir("articles/technology/training")

articles = []
genres = []
item = 1


while(item <= 100):
    file2read = open("TrTechnologyArticle" + str(item) +
                     ".txt", 'r').read().replace("\n", "")
    articles.append(file2read)
    genres.append("technology")
    item += 1

item = 1

os.chdir("../../sports/training")

while(item <= 100):
    file2read = open("TrSportsArticle" + str(item) +
                     ".txt", 'r').read().replace("\n", "")
    articles.append(file2read)
    genres.append("Sports")
    item += 1


trainingData = {'article':  articles,
                'genre': genres
                }

print(articles[2])

os.chdir("../../../")


trainingData = pd.DataFrame(trainingData)
print(trainingData)


temp = os.getcwd()
print(temp)
os.chdir("articles/technology/testing")
temp = os.getcwd()


articles = []
genres = []
item = 101


os.getcwd


while(item >= 101 and item <= 200):
    file2read = open("TeTechnologyArticle" + str(item) +
                     ".txt", 'r').read().replace("\n", "")
    articles.append(file2read)
    genres.append("technology")
    item += 1

item = 101

os.chdir("../../sports/testing")

while(item >= 101 and item <= 200):
    file2read = open("TeSportsArticle" + str(item) +
                     ".txt", 'r').read().replace("\n", "")
    articles.append(file2read)
    genres.append("Sports")
    item += 1


testingData = {'article':  articles,
               'genre': genres
               }

print(articles[2])

os.chdir("../../../")


testingData = pd.DataFrame(testingData)
print(testingData)
