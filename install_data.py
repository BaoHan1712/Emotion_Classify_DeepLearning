from datasets import load_dataset

# Tải dataset
ds = load_dataset("uitnlp/vietnamese_students_feedback")

#  Xem thông tin cơ bản
print(ds)

# Lưu toàn bộ dataset về máy dưới dạng CSV
for split in ds.keys():
    filename = f"vietnamese_students_feedback_{split}.csv"
    ds[split].to_csv(filename)
    print(f"✅ Đã lưu: {filename}")
