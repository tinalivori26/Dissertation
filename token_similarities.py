from gensim.models import Word2Vec

#loading the Word2Vec models
model1 = Word2Vec.load("raw_all_model")
model2 = Word2Vec.load("raw_emoji_model")
model3 = Word2Vec.load("clean_all_model")
model4 = Word2Vec.load("clean_emoji_model")


#analysing the top 10 emojis in model1
print("RAW ALL DATASET")
print("😂", model1.wv.most_similar("😂", topn=50))
print("❤", model1.wv.most_similar("❤", topn=50))
print("💙", model1.wv.most_similar("💙", topn=50))
print("🙈", model1.wv.most_similar("🙈", topn=50))
print("🎶", model1.wv.most_similar("🎶", topn=50))
print("🍕", model1.wv.most_similar("🍕", topn=50))
print("🙉", model1.wv.most_similar("🙉", topn=50))
print("🙊", model1.wv.most_similar("🙊", topn=50))
print("🐶", model1.wv.most_similar("🐶", topn=50))
print("😍", model1.wv.most_similar("😍", topn=50))
print()

#analysing the top 10 emojis in model2
print("ONLY EMOJI DATASET")
print("😂", model2.wv.most_similar("😂", topn=50))
print("❤", model2.wv.most_similar("❤", topn=50))
print("💙", model2.wv.most_similar("💙", topn=50))
print("🙈", model2.wv.most_similar("🙈", topn=50))
print("🎶", model2.wv.most_similar("🎶", topn=50))
print("🍕", model2.wv.most_similar("🍕", topn=50))
print("🙉", model2.wv.most_similar("🙉", topn=50))
print("🙊", model2.wv.most_similar("🙊", topn=50))
print("🐶", model2.wv.most_similar("🐶", topn=50))
print("😍", model2.wv.most_similar("😍", topn=50))
print()

#analysing the top 10 emojis in model3
print("CLEAN ALL DATASET")
print("😂", model3.wv.most_similar("😂", topn=50))
print("❤", model3.wv.most_similar("❤", topn=50))
print("💙", model3.wv.most_similar("💙", topn=50))
print("🙈", model3.wv.most_similar("🙈", topn=50))
print("🎶", model3.wv.most_similar("🎶", topn=50))
print("🍕", model3.wv.most_similar("🍕", topn=50))
print("🙉", model3.wv.most_similar("🙉", topn=50))
print("🙊", model3.wv.most_similar("🙊", topn=50))
print("🐶", model3.wv.most_similar("🐶", topn=50))
print("😍", model3.wv.most_similar("😍", topn=50))
print()

#analysing the top 10 emojis in model4
print("CLEAN EMOJI DATASET")
print("😂", model4.wv.most_similar("😂", topn=50))
print("❤", model4.wv.most_similar("❤", topn=50))
print("💙", model4.wv.most_similar("💙", topn=50))
print("🙈", model4.wv.most_similar("🙈", topn=50))
print("🎶", model4.wv.most_similar("🎶", topn=50))
print("🍕", model4.wv.most_similar("🍕", topn=50))
print("🙉", model4.wv.most_similar("🙉", topn=50))
print("🙊", model4.wv.most_similar("🙊", topn=50))
print("🐶", model4.wv.most_similar("🐶", topn=50))
print("😍", model4.wv.most_similar("😍", topn=50))
