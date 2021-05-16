import json
from nltk import FreqDist
from emoji import UNICODE_EMOJI
EN_EMOJI = UNICODE_EMOJI["en"]


#function to read in the .json file datasets
def read_files(directory):
    with open(directory, mode="r", encoding="utf8") as json_file:
        return json.load(json_file)


#building a word frequency distribution
def freq(tweet_list):
    freq_dist = FreqDist(token for tweet in tweet_list for token in tweet if token.isalpha())
    return freq_dist


#building an emoji frequency distribution
def e_freq(tweet_list):
    freq_dist = FreqDist(token for tweet in tweet_list for token in tweet if token in EN_EMOJI)
    return freq_dist


#retrieving word tokens in a list
def word_list(tweet_list):
    word_tokens = [token for tweet in tweet_list for token in tweet if token.isalpha()]
    return word_tokens


#retrieving emoji tokens in a list
def emoji_list(tweet_list):
    emoji_tokens = [token for tweet in tweet_list for token in tweet if token in EN_EMOJI]
    return emoji_tokens


#directories of the 4 different datasets
read_dir_1 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/raw_all.json"
read_dir_2 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/only_emojis.json"
read_dir_3 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/clean_all.json"
read_dir_4 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/tweets/clean_emojis.json"

#reading in the .json file datasets
raw_all_data = read_files(read_dir_1)
only_emoji_data = read_files(read_dir_2)
clean_all_data = read_files(read_dir_3)
clean_emoji_data = read_files(read_dir_4)

#finding the word tokens
raw_all_words = word_list(raw_all_data)
only_emoji_words = word_list(only_emoji_data)
clean_all_words = word_list(clean_all_data)
clean_emoji_words = word_list(clean_emoji_data)

#finding unique word tokens count
print("WORD TOKENS COUNT")
print(len(set(raw_all_words)))
print(len(set(only_emoji_words)))
print(len(set(clean_all_words)))
print(len(set(clean_emoji_words)))
print()

#finding the word frequency distribution for the various datasets
raw_all_fd = freq(raw_all_data)
only_emoji_fd = freq(only_emoji_data)
cleaned_all_fd = freq(clean_all_data)
cleaned_emoji_fd = freq(clean_emoji_data)

#finding the 10 most common words
print("10 MOST FREQUENT WORDS")
print(raw_all_fd.most_common(10))
print(only_emoji_fd.most_common(10))
print(cleaned_all_fd.most_common(10))
print(cleaned_emoji_fd.most_common(10))
print()

#finding the emoji tokens
raw_all_emojis = emoji_list(raw_all_data)
raw_emoji_emojis = emoji_list(only_emoji_data)
clean_all_emojis = emoji_list(clean_all_data)
clean_emoji_emojis = emoji_list(clean_emoji_data)

#finding unique emoji tokens count
print("EMOJI TOKENS COUNT")
print(len(set(raw_all_emojis)))
print(len(set(raw_emoji_emojis)))
print(len(set(clean_all_emojis)))
print(len(set(clean_emoji_emojis)))
print()

#finding the emoji frequency distribution for the various datasets
raw_all_e_fd = e_freq(raw_all_data)
only_emoji_e_fd = e_freq(only_emoji_data)
cleaned_all_e_fd = e_freq(clean_all_data)
cleaned_emoji_e_fd = e_freq(clean_emoji_data)

#finding the 10 most common emojis
print("10 MOST FREQUENT EMOJIS")
print(raw_all_e_fd.most_common(10))
print(only_emoji_e_fd.most_common(10))
print(cleaned_all_e_fd.most_common(10))
print(cleaned_emoji_e_fd.most_common(10))
print()

#finding the 20 most common words
print("20 MOST FREQUENT EMOJIS")
print(only_emoji_e_fd.most_common(20))
