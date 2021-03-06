import tweepy 
import pandas as pd
import json

#loading the .csv file containing my credentials
credentials_df = pd.read_csv("credentials.csv", header=None, names=["item", "key"])

consumer_key = credentials_df.loc[credentials_df["item"] == "consumer_key", "key"].iloc[0]
consumer_secret = credentials_df.loc[credentials_df["item"] == "consumer_secret", "key"].iloc[0]
access_token = credentials_df.loc[credentials_df["item"] == "access_token", "key"].iloc[0]
access_token_secret = credentials_df.loc[credentials_df["item"] == "access_secret", "key"].iloc[0]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#intialising variables necessary to scrape the tweet details
coordinates = "35.8997,14.5147,15mi"
max_tweets = 18000

#creating a query method using parameters
tweets = tweepy.Cursor(api.search, geocode=coordinates).items(max_tweets)

#pulling the chosen tweet information
tweets_list = [[tweet.text, tweet.id_str, tweet.truncated, tweet.lang, tweet.user.id_str, tweet.user.location]
               for tweet in tweets]

directory = "C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/scraped_tweets/tweets7.json"

#creating a json object to store the twitter data
json_object = json.dumps(tweets_list, indent=4)

#storing the data into a .json file
with open(directory, mode="w", encoding="utf-8") as f:
    f.write(json_object)
