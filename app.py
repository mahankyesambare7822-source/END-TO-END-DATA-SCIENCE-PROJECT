from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return "Student Score Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    hours = data["hours"]

    prediction = model.predict([[hours]])

    return jsonify({
        "study_hours": hours,
        "predicted_score": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)