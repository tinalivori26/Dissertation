from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


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


#loading the Word2Vec model
model1 = Word2Vec.load("raw_emoji_model")

#list of top 20 words and emojis
top_tokens = ["😂", "❤", "💙", "🙈", "🎶", "🍕", "🙉", "🙊", "🐶", "😍", "☀", "😊", "😭", "🤣", "🏻", "👊", "🙏", "🏼",
              "😆", "😘"]

#plotting the top data retrieved from the model
tsne_plot(model1, top_tokens)
