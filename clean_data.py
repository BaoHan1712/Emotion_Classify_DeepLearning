import pandas as pd

# Đọc dữ liệu gốc
df = pd.read_csv(r"dataset\vietnamese_students_feedback_train.csv")
# Giữ lại 2 cột cần thiết
df = df[["sentence", "sentiment"]]

# Xuất ra file CSV mới
output_path = "feedback_train_clean.csv"
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"✅ Đã lưu dataset mới tại: {output_path}")
print(df.head())
