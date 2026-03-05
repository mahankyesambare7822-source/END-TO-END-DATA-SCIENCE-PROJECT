import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("data/student_scores.csv")

# Input feature
X = data[["Hours"]]

# Target output
y = data["Score"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save trained model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")