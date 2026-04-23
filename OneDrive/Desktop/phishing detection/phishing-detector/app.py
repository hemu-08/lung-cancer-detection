from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    print("Data received:", data)
    features = [[int(data["SMOKING"]), int(data["YELLOW_FINGERS"]), int(data["ANXIETY"]),
                 int(data["PEER_PRESSURE"]), int(data["CHRONIC_DISEASE"]), int(data["FATIGUE"]),
                 int(data["ALLERGY"]), int(data["WHEEZING"])]]
    pred = model.predict(features)[0]
    prob = round(float(model.predict_proba(features)[0][1]) * 100, 2)
    result = "HIGH RISK - Lung Cancer Detected" if pred == 1 else "LOW RISK - No Lung Cancer Detected"
    print("Result:", result)
    return jsonify({"result": result, "probability": prob})

if __name__ == "__main__":
    app.run(debug=False)