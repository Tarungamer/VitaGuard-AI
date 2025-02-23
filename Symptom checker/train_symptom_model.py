import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("T:\\TARUN LEARNING\\VITAGUARD AI APP\\SymbiPredict\\symbipredict_2022.csv")

# Encode categorical disease labels
label_encoder = LabelEncoder()
df["prognosis"] = label_encoder.fit_transform(df["prognosis"])

# Define features (X) and target (y)
X = df.drop(columns=["prognosis"])
y = df["prognosis"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save Model & Encoder
joblib.dump(model, "T:\\TARUN LEARNING\\VITAGUARD AI APP\\Symptom checker\\models\\disease_predictor.pkl")
joblib.dump(label_encoder, "T:\\TARUN LEARNING\\VITAGUARD AI APP\\Symptom checker\\models\\label_encoder.pkl")

print("Model trained and saved!")
