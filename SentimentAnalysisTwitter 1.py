from textblob import TextBlob                                           #1 Algorithm
import tweepy as tw
import sys
import matplotlib.pyplot as plt
import api
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer    #2 Algorithm

#api key can be obtained through twitter developer website
api_key=''
api_key_secret=''
access_token=''
access_token_secret=''

auth_handler=tw.OAuth1UserHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)

#Api=api.search(auth_handler)
api=tw.API(auth_handler)

search_term=str(input("Search Trending topics on Twitter:"))
tweet_amt=int(input("Enter the number of tweets you want to see:"))
tweets=tw.Cursor(api.search_tweets,q=search_term,lang='en').items(tweet_amt)

print("There are 2 algorithms to select \n1.TextBlob\n2.VADER\n3.See tweets:")
choice=int(input("Select your choice according to the serial number:"))
polarity=0
positive=0
negative=0
neutral=0
#For vader
polar_neg=0
polar_pos=0
polar_neu=0
#Sentiment analysis
#for tweet in tweets:
    #print(tweet.text)
#    final_tweet=tweet.text.replace('RT', '')
#    if final_tweet.startswith(' @'):
#        position=final_tweet.index(':')
#        final_tweet=final_tweet[position+2:]
#    if final_tweet.startswith('@'):
#        position=final_tweet.index(' ') 
#        final_tweet=final_tweet[position+2:]
if choice==1:
    for tweet in tweets:
    #print(tweet.text)
        final_tweet=tweet.text.replace('RT', '')
        if final_tweet.startswith(' @'):
            position=final_tweet.index(':')
            final_tweet=final_tweet[position+2:]
        if final_tweet.startswith('@'):
            position=final_tweet.index(' ') 
            final_tweet=final_tweet[position+2:]
    
        analysis=TextBlob(final_tweet)
        tweet_polarity=analysis.polarity
        if tweet_polarity>0:
            positive+=1
        elif tweet_polarity<0:
            negative+=1
        else:
            neutral+=1
        polarity+=tweet_polarity

    print(polarity) #if>0 then more amount of positive tweets.
    print(f"The amount of positive tweets are {positive}.")
    print(f"The amount of negative tweets are {negative}.")
    print(f"The amount of neutral tweets are {neutral}.")

#Visualization

# creating the dataset
    sentiment= ['positive', 'negative', 'neutral']
    values= [positive,negative,neutral]


# Creating a bar chart
    plt.bar(sentiment[0], values[0],color='g',label='positive')
    plt.bar(sentiment[1], values[1],color='r',label='negative')
    plt.bar(sentiment[2], values[2],color='b',label='neutral')

    plt.title(f'Sentiment analysis of tweets:{search_term}')
    plt.xlabel('Sentiments', fontsize=16)
    plt.ylabel('Frequency', fontsize=16)
    plt.legend(["positive", "negative","neutral"],bbox_to_anchor=(1,1),loc ="upper left")
    plt.grid(True)
    plt.show()


elif choice==2:
    for tweet in tweets:
    #print(tweet.text)
        final_tweet=tweet.text.replace('RT', '')
        if final_tweet.startswith(' @'):
            position=final_tweet.index(':')
            final_tweet=final_tweet[position+2:]
        if final_tweet.startswith('@'):
            position=final_tweet.index(' ') 
            final_tweet=final_tweet[position+2:]

        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(final_tweet)
    #tweet_polarity=sentiment_dict.
     
    #print("Overall sentiment dictionary is : ", sentiment_dict)
    #print("Tweet was rated as ", sentiment_dict['neg']*100, "% Negative")
    #print("Tweet was rated as ", sentiment_dict['neu']*100, "% Neutral")
    #print("Tweet was rated as ", sentiment_dict['pos']*100, "% Positive")
 
    #print("Tweet Overall Rated As", end = " ")
 
    # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05 :
            positive+=1
            #print("Positive Tweet!")
 
        elif sentiment_dict['compound'] <= - 0.05 :
            negative+=1
            #print("Negative tweet!")
 
        else :
            neutral+=1
            #print("Neutral tweet!")
        polar_neg+=sentiment_dict.get('neg')
        polar_pos+=sentiment_dict.get('pos')
        polar_neu+=sentiment_dict.get('neu')

    print(f"Negative polarity={polar_neg}\nPositive polarity{polar_pos}\nNeutral polarity={polar_neu}") #if>0 then more amount of positive tweets.
    print(f"The amount of positive tweets are {positive}.")
    print(f"The amount of negative tweets are {negative}.")
    print(f"The amount of neutral tweets are {neutral}.")

#Visualization

# creating the dataset
    sentiment= ['positive', 'negative', 'neutral']
    values= [positive,negative,neutral]


# Creating a bar chart
    plt.bar(sentiment[0], values[0],color='g',label='positive')
    plt.bar(sentiment[1], values[1],color='r',label='negative')
    plt.bar(sentiment[2], values[2],color='b',label='neutral')

    plt.title(f'Sentiment analysis of tweets:{search_term}')
    plt.xlabel('Sentiments', fontsize=16)
    plt.ylabel('Frequency', fontsize=16)
    plt.legend(["positive", "negative","neutral"],bbox_to_anchor=(1,1),loc ="upper left")
    plt.grid(True)
    plt.show()

 

elif choice==3:
    for tweet1 in tweets:   #calculated the number of iterations using enumerate!
        for iteration, tweet1 in enumerate(tweets):
        
            print(f"Printing tweets {iteration}:")
            print(tweet1.text)
else:
    print("Select from given options!")










    
