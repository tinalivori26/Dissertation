import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

#locating the area of Malta
loc = "35.8997, 14.5147, 15mi"

#scraping tweets by users in the area of Malta into a dataframe
df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('geocode:"{}"'.format(loc)).get_items(), 500000))[[
    "content", "id", "renderedContent", "lang", "user", "date"]]

#adding the user id and location to the data frame
df["userId"] = df["user"].apply(lambda x: x["id"])
df["userLocation"] = df["user"].apply(lambda x: x["location"])

#saving the dataframe in a .json file
df.to_json(r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/scraped_tweets/tweets8.json", orient="values",
           indent=4)
