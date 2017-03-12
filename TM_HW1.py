# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 23:53:16 2017

@author: CrowPeter
"""
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

lines = []
for line in open('D:/10602/TM/HW2/TM_Hw_2/building_global_community.txt'):
    line = line.strip()
    lines.append(line)

word_all = []
for line in lines: 
    word_to = word_tokenize(line)
    word_f1 = [word.lower() for word in word_to if word.isalpha()]
    stopword_e = set(stopwords.words('english'))
    word_f2 = [word for word in word_f1 if word not in stopword_e]
    word_all = word_all + word_f2
    
wordCounter = Counter(word_all)
print wordCounter.most_common(20)