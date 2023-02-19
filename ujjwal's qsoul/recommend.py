import pandas as pd
import numpy as np
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
dataf = pd.read_csv("recommend1.csv")
# data.head()
articles = dataf["Article"].tolist()
def create_soup(x):
    soup = ' '.join(x['Article'])
    return soup
dataf['soup'] = dataf.apply(create_soup, axis=1)

uni_tfidf = text.TfidfVectorizer(input=articles, stop_words="english")
uni_matrix = uni_tfidf.fit_transform(articles)
# print(uni_matrix.shape)
# print(uni_tfidf.get_feature_names()[5000:5010])
cosine_sim = cosine_similarity(uni_matrix, uni_matrix, True)
# print(cosine_sim.shape)
# print(cosine_sim)
# Reset index of main DataFrame and construct reverse mapping as before
metadata = dataf.reset_index()
indices = pd.Series(metadata.index, index=metadata['Title']).drop_duplicates()
# print(indices[:10])

# Function that takes in article title as input and outputs most similar articles
def get_recommendations(title, indices, cosine_sim, data):
    # Get the index of the article that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all articles with that article
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the articles based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar articles
    sim_scores = sim_scores[1:11]

    # Get the article indices
    article_indices = [i[0] for i in sim_scores]
    print("Articles related to '%s' are :" %title, end="\n")
    # Return the top 10 most similar articles
    return data['Title'].iloc[article_indices]

print(get_recommendations('how to become a human', indices, cosine_sim, metadata))

    # GArbage
# def recommend_articles(x):
#     return ", ".join(data["Title"].loc[x.argsort()[-5:-1]])    
# data["Recommended Articles"] = [recommend_articles(x) for x in uni_sim]
# # data.head()
# print(data["Recommended Articles"][35])