# topic_modeling_tfidf
Topic Modelling Optimization in Chinese News Article


Objective
---------------------------------------------
This project intends to find a fast way to identify the keywords in the news article. Based on the feature of the news article, term frequency-inverse document frequency (TF-IDF) allows quick use of new keywords identified and fixes the trends of using new words/ new phrases in news.

In this project, IDF is calculated by using the articles in Wikipedia. The adoption of TFIDF is fast and more accurate than using only a few articles in recent time, which would enlarge IDF when some hot topics are frequently discussed.



Limitation
---------------------------------------------
Using TFIDF alone is not recommended for topic modeling in news topic. Other factors like trendiness, the coexistence of keywords and noise of some common words would also be considered when constructing a topic model.

For any inquiries, please contact me at adam.kc.chin@gmail.com.






















License
----------------------------------------------
MIT License

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
SOFTWARE.
