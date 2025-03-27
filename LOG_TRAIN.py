import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
file_path = "train_strip.csv"  # Update with your file path
df = pd.read_csv(file_path)

# Extract features and target
X = df["Utterance"]
y = df["Emotion"]

# Convert text data into TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")

# Get unique emotion labels
labels = sorted(y.unique())

# Confusion Matrix Visualization (Fixing labels)
conf_matrix = confusion_matrix(y_test, y_pred, labels=labels)
plt.figure(figsize=(10, 6))
plt.imshow(conf_matrix, cmap="Blues", interpolation='nearest')
plt.colorbar()
plt.xticks(ticks=range(len(labels)), labels=labels, rotation=45)
plt.yticks(ticks=range(len(labels)), labels=labels)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Bar Chart for Predicted Emotions
y_pred_series = pd.Series(y_pred)
y_pred_counts = y_pred_series.value_counts()
plt.figure(figsize=(8, 5))
plt.bar(y_pred_counts.index, y_pred_counts.values, color="blue")
plt.xlabel("Predicted Emotion")
plt.ylabel("Count")
plt.title("Distribution of Predicted Emotions")
plt.xticks(rotation=45)
plt.show()
