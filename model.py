import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

try:
    df = pd.read_csv('data.csv')
    print("Columns:", df.columns.tolist())
except FileNotFoundError:
    print("Error: data.csv not found")
    exit()
except Exception as e:
    print(f"Error reading data.csv: {e}")
    exit()

print(df.head())

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])
pipeline.fit(df['Question'], df['Category'])

joblib.dump(pipeline, 'chat_categorizer.pkl')












