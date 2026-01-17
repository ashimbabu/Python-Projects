import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

print("===== Email Spam Detector =====")

# Load dataset (TAB-separated)

try:
    data = pd.read_csv(
        "emails.csv",
        encoding="latin-1",
        sep="\t",
        engine="python"
    )
except FileNotFoundError:
    print("Error: emails.csv not found.")
    exit()
except Exception as e:
    print("Error loading dataset:", e)
    exit()

print("Dataset Shape:", data.shape)
print("Columns:", list(data.columns))

# Validate columns

if not {"text", "label"}.issubset(data.columns):
    print("Error: CSV must contain 'text' and 'label' columns.")
    exit()

# Data cleaning

data = data.dropna(subset=["text", "label"])
data["text"] = data["text"].astype(str).str.strip()
data["label"] = data["label"].astype(str).str.strip()
data = data[(data["text"] != "") & (data["label"] != "")]

if data["label"].nunique() < 2:
    print("Error: Dataset must contain both spam and ham emails.")
    exit()

# Features & labels

X = data["text"]
y = data["label"]

# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Text vectorization

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    max_df=0.95
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes model

model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluation

y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Real-time prediction

while True:
    email_text = input("\nEnter email text (type 'exit' to quit): ").strip()
    if email_text.lower() == "exit":
        print("Exiting Email Spam Detector.")
        break

    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]

    print("Prediction:", prediction.upper())
