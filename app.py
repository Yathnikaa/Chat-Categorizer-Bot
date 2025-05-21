from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    model = joblib.load("chat_categorizer.pkl")
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise

@app.route("/categorize", methods=["POST"])
def categorize():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    prediction = model.predict([message])[0]
    logging.debug(f"Message: {message}, Prediction: {prediction}")
    logging.info(f"Message: {message}, Prediction: {prediction}")
    return jsonify({"category": prediction})

if __name__ == "__main__":
    app.run(debug=True)
