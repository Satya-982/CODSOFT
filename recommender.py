import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, dataframe):
        self.df = dataframe
        # Combine genres and descriptions into a single metadata profile string
        self.df['metadata'] = self.df['genres'] + " " + self.df['description']
        
        # Initialize TF-IDF Vectorizer and strip out common English stop words
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['metadata'])
        
        # Calculate the pairwise cosine similarity matrix
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        
    def get_recommendations(self, movie_title, top_n=3):
        # Case-insensitive search match
        movie_title_lower = movie_title.lower()
        matching_indices = self.df[self.df['title'].str.lower() == movie_title_lower].index
        
        if len(matching_indices) == 0:
            return None
        
        idx = matching_indices[0]
        
        # Fetch the pairwise similarity scores for the chosen movie
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        
        # Sort movies based on highest similarity score
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Slice top_n scores (skipping the index 0 element because it is the movie itself)
        sim_scores = [score for score in sim_scores if score[0] != idx][:top_n]
        
        # Gather the actual dataframe indices of the top matches
        movie_indices = [i[0] for i in sim_scores]
        
        # Return a dictionary format containing the top recommended movie titles and genres
        return self.df.iloc[movie_indices][['title', 'genres']].to_dict(orient='records')