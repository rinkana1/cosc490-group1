import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("dev_strip.csv")

# Text Preprocessing
stop_words = set(ENGLISH_STOP_WORDS)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)  # Remove non-word characters
    words = text.split()  # Tokenize by splitting
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

df['clean_text'] = df['Utterance'].apply(preprocess_text)

# Convert labels to numerical format
labels = df['Emotion'].astype('category').cat.codes

# Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['clean_text'])
y = labels

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
