from nltk.corpus import stopwords
import re
import string
from nltk.stem import WordNetLemmatizer
from emoji import UNICODE_EMOJI
from nltk import FreqDist
import json
from nltk.tokenize.casual import TweetTokenizer
EN_EMOJI = UNICODE_EMOJI['en']


#removing stopwords, urls, punctuation, and implementing lower casing, lemmatization
def preprocessing(tweet):
    #stopword removal using the established set of stopwords for English
    stop_words = set(stopwords.words("english"))
    no_stop_list = [token for token in tweet if token not in stop_words]
    #url removal
    no_url_list = [re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE) for tweet in no_stop_list]
    #punctuation removal
    no_punctuation_list = [token.translate(str.maketrans('', '', string.punctuation)) for token in no_url_list]
    #lowercasing
    case_fold_list = [token.casefold() for token in no_punctuation_list]
    #lemmatization
    wnl = WordNetLemmatizer()
    lemmas_list = [wnl.lemmatize(token, pos="a") for token in case_fold_list]
    return lemmas_list


#creating a function that returns tweets if they contain an emoji
def emoji_tweet(tweet):
    count = 0
    for token in tweet:
        if token in EN_EMOJI:
            count += 1
    if count != 0:
        return tweet


#building a word frequency distribution
def freq(tweet_list):
    freq_dist = FreqDist(token for tweet in tweet_list for token in tweet if token.isalpha())
    return freq_dist


#building an emoji frequency distribution
def e_freq(tweet_list):
    freq_dist = FreqDist(token for tweet in tweet_list for token in tweet if token in EN_EMOJI)
    return freq_dist


#writing the dataset into .json files
def write_files(directory, tweets):
    json_object = json.dumps(tweets, indent=4)
    with open(directory, mode="w", encoding="utf-8") as f:
        f.write(json_object)


read_directory = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/tweets.json"

#reading in the .json file with the scraped tweets
with open(read_directory, mode="r", encoding="utf8") as json_file:
    data = json.load(json_file)

#making a list of tweets and their language, storing them as tuples
tweets_list = [(item[0], item[3]) for item in data]
print(len(tweets_list))

#retrieving those tweets which are in english only
english_tweets = [pair[0] for pair in tweets_list if pair[1] == "en"]

#tokenizing the retrieved tweets - the raw_all_tweets dataset
tokenized_en_tweets = [TweetTokenizer().tokenize(tweet) for tweet in english_tweets if len(english_tweets) != 0]
print(len(tokenized_en_tweets))

#saving tweets with an emoji - the only_emoji_tweets dataset
emoji_tweet_list = [emoji_tweet(tweet) for tweet in tokenized_en_tweets if emoji_tweet(tweet) is not None]
print(len(emoji_tweet_list))

#preprocessing the tweets using the preprocessing function - the cleaned_all_tweets dataset
cleaned_all_tweets = [preprocessing(tweet) for tweet in tokenized_en_tweets]

#preprocessing the tweets using the preprocessing function - the cleaned_emoji_tweets dataset
cleaned_emoji_tweets = [preprocessing(tweet) for tweet in emoji_tweet_list]
    
#find the word frequency distribution for the various datasets
raw_all_fd = freq(tokenized_en_tweets)
only_emoji_fd = freq(emoji_tweet_list)
cleaned_all_fd = freq(cleaned_all_tweets)
cleaned_emoji_fd = freq(cleaned_emoji_tweets)

print(raw_all_fd.most_common(10))
print(only_emoji_fd.most_common(10))
print(cleaned_all_fd.most_common(10))
print(cleaned_emoji_fd.most_common(10))
print()

#find the emoji frequency distribution for the various datasets
raw_all_e_fd = e_freq(tokenized_en_tweets)
only_emoji_e_fd = e_freq(emoji_tweet_list)
cleaned_all_e_fd = e_freq(cleaned_all_tweets)
cleaned_emoji_e_fd = e_freq(cleaned_emoji_tweets)

print(raw_all_e_fd.most_common(10))
print(only_emoji_e_fd.most_common(10))
print(cleaned_all_e_fd.most_common(10))
print(cleaned_emoji_e_fd.most_common(10))

#directories to save the 4 different datasets into
write_dir_1 = "C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/raw_all.json"
write_dir_2 = "C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/only_emojis.json"
write_dir_3 = "C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/clean_all.json"
write_dir_4 = "C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/clean_emojis.json"

#write the data into the .json file
write_files(write_dir_1, tokenized_en_tweets)
write_files(write_dir_2, emoji_tweet_list)
write_files(write_dir_3, cleaned_all_tweets)
write_files(write_dir_4, cleaned_emoji_tweets)
