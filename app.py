import json
import os
from pathlib import Path

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest


PROJECT_NAME = "student-ml-api"
VERSION_FILE = Path(__file__).with_name("VERSION")


def read_version():
    return VERSION_FILE.read_text(encoding="utf-8").strip()


app = Flask(__name__)


@app.get("/health")
def health():
    version = read_version()
    if version.startswith("1.1."):
        return jsonify(
            {
                "status": "healthy",
                "application": PROJECT_NAME,
                "application_version": version,
                "model_version": os.getenv("MODEL_VERSION", "model-1"),
            }
        )
    return jsonify(
        {
            "status": "healthy",
            "application": PROJECT_NAME,
            "version": version,
        }
    )


@app.post("/predict")
def predict():
    if not request.is_json:
        return jsonify({"error": "request body must be valid JSON"}), 400

    try:
        payload = request.get_json(silent=False)
    except BadRequest:
        return jsonify({"error": "request body must be valid JSON"}), 400
    if not isinstance(payload, dict):
        return jsonify({"error": "request body must be a JSON object"}), 400
    if "value" not in payload:
        return jsonify({"error": "missing required field: value"}), 400

    value = payload["value"]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return jsonify({"error": "value must be a number"}), 400

    return jsonify({"input": value, "prediction": value * 2}), 200


@app.errorhandler(405)
def method_not_allowed(_error):
    return jsonify({"error": "method not allowed"}), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
