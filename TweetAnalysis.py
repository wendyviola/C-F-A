# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:37:01 2022

@author: Admin
"""
#Importing packages to be used
import twint
import nest_asyncio

nest_asyncio.apply()
# Configure
c = twint.Config()
c.Search = "#RacistEU"
#c.Retweets = True
c.Since = '2022-02-26'
c.Until = '2022-03-26'
c.Count = True #total number of hashtags fetched
c.Store_csv = True
c.Debug = True
c.Output = "Twitter Data"
# Run
twint.run.Search(c)

import pandas as pd
df = pd.read_csv("C:\\Users\\Admin\\Twitter Data\\tweets.csv")
df.tail()

#plottting graph
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

matplotlib.pyplot.title("#RacistEU Hahstag")
matplotlib.pyplot.xlabel("Date")
matplotlib.pyplot.ylabel("count of tweets")

import pandas as pd
df = pd.read_csv("C:\\Users\\Admin\\Twitter Data\\tweets.csv")

 
# Plotting the time series of given dataframe 

df = pd.DataFrame({'date': np.array([datetime.datetime(2022, 3, i+1)
                                     for i in range(12)]),
                   'tweets': [3, 20, 30, 50, 100, 200, 300, 600, 700, 1000, 1200, 1300]})
df['date'].value_counts().plot()
#plot time series
plt.plot(df.date, df.tweets, linewidth=3)

#wordcloud
import wordcloud
import wikipedia

result= wikipedia.page("#RacistEU")
final_result = result.content
print(final_result)
result= wikipedia.summary("#RacistEU", sentences=10)
print(result)

#Developing the Wordcloud

import nltk # Natural Language ToolKit
nltk.download('stopwords')
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud 


def plot_cloud(wordcloud):
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud) 
    plt.axis("off");
wordcloud = WordCloud(width = 500, height = 500, background_color='pink', random_state=10).generate(final_result)
plot_cloud(wordcloud)