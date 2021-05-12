import json

read_directory = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/tweets.json"

#reading in the .json file with the scraped tweets
with open(read_directory, mode="r", encoding="utf8") as json_file:
    data = json.load(json_file)

#making a list of tweet IDs
tweet_ids = [(item[1]) for item in data]

write_directory = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/tweet_ids.json"

#creating a json object to store the tweet IDs
json_object = json.dumps(tweet_ids, indent=4)

#storing the IDs into a .json file
with open(write_directory, mode="w", encoding="utf-8") as f:
    f.write(json_object)
