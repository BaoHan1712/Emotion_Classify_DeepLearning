import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# ======== 1️⃣ Load mô hình và tokenizer ========
SAVE_DIR = "phobert_sentiment_model"  # Thư mục chứa model đã lưu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("🔄 Loading model from:", SAVE_DIR)
tokenizer = AutoTokenizer.from_pretrained(SAVE_DIR)
model = AutoModelForSequenceClassification.from_pretrained(SAVE_DIR)
model.to(device)
model.eval()

# ======== 2️⃣ Các nhãn ========
id2label = {0: "negative", 1: "neutral", 2: "positive"}

# ======== 3️⃣ Hàm dự đoán ========
def predict_sentiment(text):
    # Tiền xử lý và mã hóa
    inputs = tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=128,
        return_tensors="pt"
    ).to(device)

    # Dự đoán
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=-1)
        pred_id = torch.argmax(probs, dim=-1).item()

    label = id2label[pred_id]
    confidence = probs[0][pred_id].item()
    return label, confidence

# ======== 4️⃣ Chạy thử ========
if __name__ == "__main__":
    print("✅ PhoBERT Sentiment Model loaded successfully!")

    while True:
        text = input("\nNhập câu cần phân tích cảm xúc (hoặc gõ 'exit' để thoát): ")
        if text.lower() == "exit":
            break
        label, conf = predict_sentiment(text)
        print(f"🧠 Cảm xúc dự đoán: {label.upper()} (độ tin cậy: {conf:.2%})")
