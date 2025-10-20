from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

app = Flask(__name__)
CORS(app)  
# =========================
# Load model & tokenizer
# =========================
SAVE_DIR = "phobert_sentiment_model"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("🔄 Loading PhoBERT model from:", SAVE_DIR)
tokenizer = AutoTokenizer.from_pretrained(SAVE_DIR)
model = AutoModelForSequenceClassification.from_pretrained(SAVE_DIR)
model.to(device)
model.eval()

id2label = {0: "negative", 1: "neutral", 2: "positive"}

# =========================
#  Hàm dự đoán cảm xúc
# =========================
def predict_sentiment(text: str):
    if not text or not text.strip():
        return None, 0.0

    inputs = tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=128,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred_id = torch.argmax(probs, dim=-1).item()

    label = id2label[pred_id]
    confidence = probs[0][pred_id].item()
    return label, confidence

# =========================
# API endpoint
# =========================
@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON"}), 400

    text = data["text"]
    label, conf = predict_sentiment(text)
    if label is None:
        return jsonify({"error": "Empty text"}), 400
    print(f"😎 Input: {text} => Predicted: {label} (Confidence: {conf:.4f})")

    return jsonify({
        "text": text,
        "sentiment": label,
        "confidence": round(conf, 4)
    })

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
