import pandas as pd

# Đường dẫn tới file CSV
file_path = r"data_clean\feedback_valid_clean.csv"

# Đọc dữ liệu
df = pd.read_csv(file_path)

print("📋 Xem trước dữ liệu:")
print(df.head())

# Kiểm tra các cột có đúng không
print("\n📦 Các cột có trong file:", list(df.columns))

# Đếm số lượng từng nhãn cảm xúc
label_counts = df['sentiment'].value_counts().sort_index()

# Gán nhãn
labels = {
    0: "Negative (Tiêu cực)",
    1: "Neutral (Trung lập)",
    2: "Positive (Tích cực)"
}

print("\n📊 Thống kê dữ liệu cảm xúc:")
for label, meaning in labels.items():
    count = label_counts.get(label, 0)
    print(f"{label} - {meaning}: {count} mẫu")

# Tổng số dòng
print(f"\nTổng số mẫu trong tập dữ liệu: {len(df)}")
