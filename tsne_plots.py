import json
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


#function to read in the .json file datasets
def read_files(directory):
    with open(directory, mode="r", encoding="utf8") as json_file:
        return json.load(json_file)


#creating a TSNE model and plotting it
def tsne_plot(model, toks):
    #taking the words as the labels and their embeddings as the tokens from the saved model
    labels = [word for word in toks]
    tokens = [model.wv[word] for word in toks]

    #creating a TSNE model with the appropriate parameters
    tsne_model = TSNE(perplexity=40, n_components=2, init="pca", n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    #setting the values for the plot
    x = [value[0] for value in new_values]
    y = [value[1] for value in new_values]

    #plotting the data
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i], xy=(x[i], y[i]), xytext=(5, 2), textcoords="offset points", ha="right", va="bottom")
    plt.show()


#reading directories of emojis
read_dir_1 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/word2vec_models/top20emojis.json"
read_dir_2 = r"C:/Users/marti/OneDrive/Documents/HLT/Dissertation/code/data/word2vec_models/top100emojis.json"

#retrieving the top 20 emojis
top_20_fd = read_files(read_dir_1)
top_20_emojis = [pair[0] for pair in top_20_fd]

#retrieving the top 100 emojis
top_100_fd = read_files(read_dir_2)
top_100_emojis = [pair[0] for pair in top_100_fd]

#loading the Word2Vec model
model1 = Word2Vec.load("clean_emoji_model")

#plotting the top data retrieved from the model
tsne_plot(model1, top_20_emojis)
tsne_plot(model1, top_100_emojis)
