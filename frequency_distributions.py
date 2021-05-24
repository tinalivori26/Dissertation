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


#writing the dataset into .json files
def write_files(directory, tweets):
    json_object = json.dumps(tweets, indent=4)
    with open(directory, mode="w", encoding="utf-8") as f:
        f.write(json_object)


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

#finding the raw_all word tokens
print("RAW_ALL WORD COUNT")
raw_all_words = word_list(raw_all_data)
print("Tokens", len(raw_all_words))
print("Types", len(set(raw_all_words)))
print()

#finding the only_emoji word tokens
print("ONLY_EMOJI WORD COUNT")
only_emoji_words = word_list(only_emoji_data)
print("Tokens", len(only_emoji_words))
print("Types", len(set(only_emoji_words)))
print()

#finding the clean_all word tokens
print("CLEAN_ALL WORD COUNT")
clean_all_words = word_list(clean_all_data)
print("Tokens", len(clean_all_words))
print("Types", len(set(clean_all_words)))
print()

#finding the clean_emoji word tokens
print("CLEAN_EMOJI WORD COUNT")
clean_emoji_words = word_list(clean_emoji_data)
print("Tokens", len(clean_emoji_words))
print("Types", len(set(clean_emoji_words)))
print()

#finding the word frequency distribution
raw_all_fd = freq(raw_all_data)
only_emoji_fd = freq(only_emoji_data)
cleaned_all_fd = freq(clean_all_data)
cleaned_emoji_fd = freq(clean_emoji_data)

#finding the 10 most common words
print("10 MOST FREQUENT WORDS")
print("Raw all", raw_all_fd.most_common(10))
print("Only emoji", only_emoji_fd.most_common(10))
print("Clean all", cleaned_all_fd.most_common(10))
print("Clean emoji", cleaned_emoji_fd.most_common(10))
print()

#finding the emoji tokens
print("EMOJI COUNT")
emojis = emoji_list(raw_all_data)
print("Tokens", len(emojis))
print("Types", len(set(emojis)))
print()

#finding the emoji frequency distribution
e_fd = e_freq(raw_all_data)

#finding the 10 most common emojis
print("10 MOST FREQUENT EMOJIS")
print("Emojis", e_fd.most_common(10))
print()

#finding those emojis with a count of 1
hapax_e = e_fd.hapaxes()
print("Count of emojis with freq = 1:", len(hapax_e))

#finding those emojis with a count of 1
hapax_e = e_fd.hapaxes()
print("Count of emojis with freq = 1:", len(hapax_e))

#plotting the frequency for the 100 most frequent emoji tokens (145,000/194,738) - 74% of emojis
e_fd.plot(100)

#plotting the cumulative frequency for the 100 most frequent emoji tokens (145,000/194,738) - 74% of emojis
e_fd.plot(100, cumulative=True)

#finding the 20 most common words
top_20_emojis = e_fd.most_common(20)

#finding the 100 most common words
top_100_emojis = e_fd.most_common(100)

#writing directories of emojis
write_dir_1 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/word2vec_models/top20emojis.json"
write_dir_2 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/word2vec_models/top100emojis.json"

#writing the data into the .json file
write_files(write_dir_1, top_20_emojis)
write_files(write_dir_2, top_100_emojis)
