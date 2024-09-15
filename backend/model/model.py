import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from sklearn.cluster import AgglomerativeClustering
import joblib  # To save/load the model

# Load dataset
def load_data(filepath):
    df = pd.read_csv(filepath)  # Corrected to use the provided filepath
    return df

# Train a clustering model (KMeans)
def train_kmeans_model(x, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    model = kmeans.fit(x)
    return model

# Train an agglomerative clustering model
def train_agglomerative_model(x, n_clusters=3):
    clustering = AgglomerativeClustering(n_clusters=n_clusters)
    clustering.fit(x)
    return clustering

# Assign cluster labels to the data
def assign_clusters(model, x):
    if hasattr(model, 'predict'):
        labels = model.predict(x)
    else:
        # For AgglomerativeClustering
        labels = model.labels_
    x['clusters'] = pd.Series(labels)
    return x

# Get career suggestions based on clusters
def get_career_recommendations(cluster_number):
    # Define predefined career categories based on clusters
    career_0 = ['Salesperson', 'Teacher', 'Nurse', 'Psychologist', 'Marketing Manager']  # Example
    career_1 = ['Accountant', 'Graphic Designer', 'Research Scientist', 'Architect']
    career_2 = ['Chef', 'Artist', 'Event Planner', 'Fashion Designer']

    career_clusters = {0: career_0, 1: career_1, 2: career_2}
    return career_clusters.get(cluster_number, [])

# Perform t-SNE for dimensionality reduction and visualization (optional, for analysis purposes)
def perform_tsne(x, n_components=3):
    tsne = TSNE(n_components=n_components, random_state=42)
    x_tsne = tsne.fit_transform(x)
    return x_tsne

# Save the trained model to disk
def save_model(model, filepath='backend/model/kmeans_model.pkl'):
    joblib.dump(model, filepath)

# Load the model from disk
def load_model(filepath='backend/model/kmeans_model.pkl'):
    model = joblib.load(filepath)
    return model

# Main function for clustering and prediction
def predict_career(input_data):
    # Load trained model (or train if not available)
    model = load_model('backend/model/kmeans_model.pkl')
    
    # Convert input data into DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Assign cluster to the input data
    if hasattr(model, 'predict'):
        input_cluster = model.predict(input_df)
    else:
        # For AgglomerativeClustering
        input_cluster = model.fit_predict(input_df)
    
    # Get career recommendations
    career_suggestions = get_career_recommendations(input_cluster[0])
    
    return career_suggestions

# Example usage:
if __name__ == "__main__":
    # Load data for training
    df = load_data("C:/Users/krish/Downloads/Data_final.csv")
    
    # Prepare data for clustering (drop target column)
    x = df.drop('Career', axis=1)
    
    # Train KMeans model
    kmeans_model = train_kmeans_model(x, n_clusters=3)
    
    # Save the trained model
    save_model(kmeans_model)
    
    # Example input data for prediction (replace with real user input in your app)
    example_input = {
        'O_score': 0.5,
        'C_score': 0.6,
        'E_score': 0.7,
        'A_score': 0.4,
        'N_score': 0.8,
        'Numerical Aptitude': 85,
        'Spatial Aptitude': 90,
        'Perceptual Aptitude': 88,
        'Abstract Reasoning': 75,
        'Verbal Reasoning': 80
    }
    
    # Predict careers based on input
    career_suggestions = predict_career(example_input)
    print("Career suggestions:", career_suggestions)
