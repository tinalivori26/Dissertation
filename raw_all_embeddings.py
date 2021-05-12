import json 
import gensim 


#function to read in the .json file datasets
def read_files(directory):
    with open(directory, mode="r", encoding="utf8") as json_file:
        return json.load(json_file)


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

#creating a model using the data
model1 = gensim.models.Word2Vec(raw_all_data, size=300, window=5, min_count=1)
model2 = gensim.models.Word2Vec(only_emoji_data, size=300, window=5, min_count=1)
model3 = gensim.models.Word2Vec(clean_all_data, size=300, window=5, min_count=1)
model4 = gensim.models.Word2Vec(clean_emoji_data, size=300, window=5, min_count=1)

#analysing the top 10 emojis in model1
print("raw_all dataset")
print("😂", model1.wv.most_similar("😂", topn=10))
print("❤", model1.wv.most_similar("❤", topn=10))
print("💙", model1.wv.most_similar("💙", topn=10))
print("🙈", model1.wv.most_similar("🙈", topn=10))
print("🎶", model1.wv.most_similar("🎶", topn=10))
print("🍕", model1.wv.most_similar("🍕", topn=10))
print("🙉", model1.wv.most_similar("🙉", topn=10))
print("🙊", model1.wv.most_similar("🙊", topn=10))
print("🐶", model1.wv.most_similar("🐶", topn=10))
print("😍", model1.wv.most_similar("😍", topn=10))
print()

#analysing the top 10 emojis in model2
print("only_emojis dataset")
print("😂", model2.wv.most_similar("😂", topn=10))
print("❤", model2.wv.most_similar("❤", topn=10))
print("💙", model2.wv.most_similar("💙", topn=10))
print("🙈", model2.wv.most_similar("🙈", topn=10))
print("🎶", model2.wv.most_similar("🎶", topn=10))
print("🍕", model2.wv.most_similar("🍕", topn=10))
print("🙉", model2.wv.most_similar("🙉", topn=10))
print("🙊", model2.wv.most_similar("🙊", topn=10))
print("🐶", model2.wv.most_similar("🐶", topn=10))
print("😍", model2.wv.most_similar("😍", topn=10))
print()

#analysing the top 10 emojis in model3
print("clean_all dataset")
print("😂", model3.wv.most_similar("😂", topn=10))
print("❤", model3.wv.most_similar("❤", topn=10))
print("💙", model3.wv.most_similar("💙", topn=10))
print("🙈", model3.wv.most_similar("🙈", topn=10))
print("🎶", model3.wv.most_similar("🎶", topn=10))
print("🍕", model3.wv.most_similar("🍕", topn=10))
print("🙉", model3.wv.most_similar("🙉", topn=10))
print("🙊", model3.wv.most_similar("🙊", topn=10))
print("🐶", model3.wv.most_similar("🐶", topn=10))
print("😍", model3.wv.most_similar("😍", topn=10))
print()

#analysing the top 10 emojis in model4
print("clean_emojis dataset")
print("😂", model4.wv.most_similar("😂", topn=10))
print("❤", model4.wv.most_similar("❤", topn=10))
print("💙", model4.wv.most_similar("💙", topn=10))
print("🙈", model4.wv.most_similar("🙈", topn=10))
print("🎶", model4.wv.most_similar("🎶", topn=10))
print("🍕", model4.wv.most_similar("🍕", topn=10))
print("🙉", model4.wv.most_similar("🙉", topn=10))
print("🙊", model4.wv.most_similar("🙊", topn=10))
print("🐶", model4.wv.most_similar("🐶", topn=10))
print("😍", model4.wv.most_similar("😍", topn=10))
print()

#saving the model into a file
model1.save("raw_all_model")
model2.save("raw_emoji_model")
model3.save("clean_all_model")
model4.save("clean_emoji_model")
