/*MIT License

Copyright (c) 2017 Adam K.C. Chin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*/

#################################################################################

import re
import MySQLdb
import os 
import codecs
import sys
from collections import Counter
from decimal import *


f = codecs.open("keywords.txt", "rb", 'utf-8"')
keywords = f.readlines()

keys_art = []
keys_art2 = []
wiki_terms = [] #final list of keywords


#Identify keywords in articles
for k in keywords:
  k = re.sub("\r\n","",k)
  if k in article:
    keys_art.append(k)

#Filter out duplicated words
for g in keys_art:
  for h in keys_art:
    if g != h:
      if h in g:
        keys_art2.append(h)

#Obtain the final list of keywords
wiki_terms = list(set(keys_art)-set(keys_art2))


#Calculate the term frequency(TF)
term_no = []
term_sum = 0
wordcount = {}
tfidf = {}

for i in xrange(len(wiki_terms)):
  term = articles.count(wiki_terms[i])
  term_no.append(term)
for i in term_no:
  term_sum = term_sum + i
for i in xrange(len(wiki_terms)):
	tf = Decimal(term_no[i])/Decimal(term_sum)
	wordcount[wiki_terms[i]]=tf
  
#Calculate the Inverse Document Frequency(IDF) by connecting the database storing the Wikipedia Documents
conn = MySQLdb.connect(
	                        host = '127.0.0.1',
	                        port = 3306,
	                        user = '',
	                        passwd = '',
	                        db = 'wikipedia',
	                        charset = 'utf8'
	                     )
x2 = conn.cursor()
for k in wiki_terms:
  x2.execute("select key_idf from key_cn where key_term = %s",(k))
  idf = x2.fetchone()
  if idf:
    tfidf_value = float(wordcount[k])* idf[0]
  if tfidf_value > 0.1:
    tfidf[k] = tfidf_value
    #if the keywords appear in header, it is important. 
    if k in articles_header:
      tfidf[k] = 1

#Top 5 keywords are selected for the article
sortedbyfrequency = sorted(tfidf, key=tfidf.get, reverse=True)
wiki_sorted=":".join(sortedbyfrequency[:5])

