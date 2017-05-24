# Sentiment-Analysis
Sentiment Analysis for Indian Premier League (IPL)

Twitter is an online microblogging and social-networking platform which allows users to write short status updates of maximum length 140 characters. According to Twitter, it is a rapidly expanding service with over 200 million registered users in which 100 million are active users and half of them tweet on a daily basis generating nearly 250 million tweets per day. Due to this large amount of usage it is possible to achieve a reflection of public sentiment by analyzing the sentiments expressed in the tweets. Sentiment analysis deals with identifying sentiments in a given source text. This project uses Tweets from the Twitter application as source data. It analyses the Tweets using machine learning techniques and classifies them as positive or negative  sentiment. IPL (Indian Premier League) being a popular cricket league in India is followed by millions of Indians and is tweeted using popular hashtags like #IPL 2017. 

Introduction:
The process of analyzing sentiments from tweets comes under "Classification". This process involves identifying "patterns" from large set of data either "supervised" or "unsupervised". In this project, machine learning techniques are used to extract the features and patterns from the data set of tweets.
Patterns can be extracted from analyzing the frequency distribution of parts of speech labeled tweets. Twitter based features relate with how people express their opinions on online social platforms and their sentiments in the limited space of 140 characters. They can include twitter hashtags, retweets, word capitalization, question marks, presence of URL in tweets, exclamation marks, internet emoticons and internet shorthand and slangs.
               Classification techniques can be divided into a two categories: Supervised vs. unsupervised. Supervised approach is the point at which we have pre-named data tests accessible and we utilize them to prepare our classifier. Training the classifier means using the pre-named dataset and extracting the features from it and identify the pattern it follows and finally model it. In case of unsupervised classification, we do not have any labeled data for training. In this technique the human (in most cases) will tell the classifier whether a particular tweet is classified correctly or not. Based on this feedback the algorithm has to learn and improve. In this project, supervised learning technique is implemented.

Functionality and design:
The way toward outlining a useful classifier for assumption examination can be separated into four fundamental classifications. They are as per the following:

1) Data Acquisition 
2) Labelling 
3) Feature Extraction 
4) Classification

1.) Data Acquisition:
Data which is in the form of tweets is acquired by using python's library named "tweepy" which provides Twitter streaming API. The streaming API facilitates programmers to filter the content based on three criteria:
• Using specific keyword(s) to track/search in the tweets
• According to specific Twitter users using their user-id’s
• Filtration based on Tweets from specific location(s)

This application sticks to the keyword (i.e., #IPL 2017) specific search criteria.
 
Before using Tweepy, a new twitter application has to be created by signing in at https://apps.twitter.com/. As a result, Twitter gives access tokens and consumer keys to connect to the streaming API.

ckey="##################"
csecret="######################################################"
atoken="######################################################"
asecret="######################################################"

The output of the above filtration returned around 60 tweets per day and data is collected over a period of 6 days.

2) Labelling:
Each tweet is labeled into two categories.

Positive: If the entire tweet has a positive/happy attitude or if something is mentioned with positive implications. Example: “Love it when @AaronFinch5 is in this mood!”.
Also if more than one sentiment is expressed in the tweet but the positive sentiment is more dominant. Example: "#IPL 2017 #Mumbai Indians: “We made a decent score even after losing our openers very early.”"
Negative: : If the entire tweet has a negative/sad/displeased attitude or if something is mentioned with negative implications. Example: "What a terrible day(s) in IPL history two of the lowest recorded scores within two days @IPL #RCBvKXIP #MIvsDD #VIVOIPL #IPL RCB #DD".
Also if more than one sentiment is expressed in the tweet but the negative sentiment is more dominant. Example: “Suddenly from d worst team @RPSupergiants are on 2nd.position”.

3) Feature Extraction:
After training set is labeled, we can extract features from it so that it can used in the classification process. Below are the text formatting techniques used to extract feature sets.
Tokenization: It is a methodology where a sentence is split into meaningful words, symbols called "tokens". NLTK (Natural Language ToolKit) provides "tokenize" library that splits a sentence of text using word space as the delimiter.
 
  Stop-words removal:
  Stop words are common words that add no significant meaning to the sentence. The NLTK corpus comes up with a set of stop words of       English language. 
  
  Stop-words include: the, a, an, ours, again, about etc.

  After removing the stop words from the tokenized tweets, the filtered sentence is framed.

  Parts-of-Speech Tagging: 
  It is the process of assigning a tag to each word in the sentence to the grammatical part of speech that word belongs to, i.e. noun,   
  verb, adjective, adverb, coordinating conjunction etc.
  NLTK Taggers package provides PerceptronTagger, we tag each token to its corresponding part of speech.
 
  
4) Classification:
Pattern classification is the process through which data is divided into different classes according to some common patterns which are found in one class to other classes. The aim of the project is to classify tweets in the following two sentiment classes: positive and negative
With Tweepy's live streaming API, latest tweets with #IPL 2017 hashtag has been collected which refers to the testing data. The testing data is fed to various classifiers provided by NLTK that calculate the accuracy percentage of each tweet.

#Training and testing using NLTK classifiers:
With NLTK's built in Naïve Bayes classifier, we check which word of the dataset appears in a positive-words-list or a negative-words-list. If the word appears in a positive words list the total score of the text is updated with plus 1 and vice versa. If at the end the total score is positive, the text is classified as positive and if it is not, the text is classified as negative. 
The variations of Naïve Bayes include MultinomialNB and BernoulliNB. 

Typically Multinomial Naive Bayes is utilized when the different events of the words matter a considerable measure in the order issue. Such an illustration is the point at which we attempt to perform Topic Classification. Bernoulli Naive Bayes can be utilized when in our issue the absence of a specific word matters. 
Linear Support Vector Classification from Sklearn.svm package provides LinearSVC classifier that are also available for classification tasks.

 
Results:
RT @IndiaToday: "I was very happy that my name got into the Champions Trophy squad" https://t.co/PIJdyKkIit - pos -0
 IPL 2017: RCB captain Virat Kohli apologises to fans neg -0
IPL 2017 Qualification Scenarios: Daredevils bow out; SRH inch closer to safety: https://t.co/COMBJ4z6Gr  pos -0
RT @IndiaToday: "I was very happy that my name got into the Champions Trophy squad" https://t.co/PIJdyKkIit - pos –1


 RT @CricketAus: David Warner's Sunrisers Hyderabad have boosted their #IPL playoff hopes with an upset win overnight https://t.co/sDydutWW2… pos –0
 RT @CricketAus: David Warner's Sunrisers Hyderabad have boosted their #IPL playoff hopes with an upset win overnight https://t.co/sDydutWW2… pos –0
David Warner's Sunrisers Hyderabad have boosted their #IPL playoff hopes with an upset win overnight… https://t.co/xp9dP2gRcH pos -0
Mumbai Indians: “They bowled well, stuck to their plans and kept us guessing.” Rohit has… https://t.co/0m89bmRS8P… https://t.co/U9Q0rZbh04 neg -0

The result of most informative features calculation is as follows:
Word	  Positive occurrence ratio	   Negative occurrence ratio
luck           3.7	                        1.0
abt	           1.0	                        2.2
msdhoni	       1.0	                        2.0
second	       1.0	                        1.8
mipaltan	     1.4	                        1.0
last	1.0	1.3
full	1.0	1.3
fabulous	1.0	1.3
less	1.0	1.3
best	1.1	1.0
orangearmy	1.1	1.0
good	1.0	1.1


Accuracy percent of each classifier:
('Original Naive Bayes Algo accuracy percent:', 57.14285714285714)
('MNB_classifier accuracy percent:', 60.317460317460316)
('BernoulliNB_classifier accuracy percent:', 60.317460317460316)
('LinearSVC_classifier accuracy percent:', 55.55555555555556)
('voted_classifier accuracy percent:', 60.317460317460316)



The above result represents the ratio of positive to negative for every word in the tweets. It can be seen that the word "luck" occurs 3.7 times more often in positive tweets than in negative tweets. 
The MultinomialNB and BernoulliNB gives the highest accuracy with 60.31 percentage compared to others.
