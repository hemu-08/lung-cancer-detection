import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv("lung_cancer_dataset.csv")

# Prepare features
df['LUNG_CANCER'] = df['LUNG_CANCER'].map({'YES': 1, 'NO': 0})
df = df.drop(columns=['visit_date'])

X = df.drop(columns=['LUNG_CANCER'])
y = df['LUNG_CANCER']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test accuracy
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")