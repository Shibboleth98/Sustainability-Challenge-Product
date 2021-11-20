import pandas
import os
import numpy as np                  #linear algebra
import pandas as pd                 # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt     #For Visualisation
import seaborn as sns               #For better Visualisation
from bs4 import BeautifulSoup
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

dir2 = 'C:\\Users\\tjshy\\Documents'

os.chdir(dir2)

#Assuming an input of differentiated words, separated by topic - what we need to do is 

#open this file and interpret it

import csv
with open("Event_Accounts.tsv", encoding='utf8') as file:
    tsv_file = csv.reader(file, delimiter="\t")
    
    
#find way to work on sample data

with open("Event_IG_5YS.tsv", encoding='utf8') as file2:
    tsv_file2 = csv.reader(file2, delimiter="\t")





###DO NOT USE THIS


#Collapse the hashtags, the 'username', 'full_name', 'biography' columns and remove everything else
#End product - x

#How to remove everything with a @
for i in x:
    translation_table = dict.fromkeys(map(ord, '!@#$'), None)
    unicode_line = unicode_line.translate(translation_table)


#Run it through VaderSentiment

pol = lambda x: analyser.polarity_scores(x)



