import pandas as pd
import random

# ====== Tập câu trung lập teen-style ======
neutral_sentences = [
"ừ", "ờ", "ờm", "uk", "ok", "oki", "okie", "uhm", "ừm", "ko sao",
    "cũng bt", "bình thường thui", "chắc zậy", "kệ đi", "đi học thôi mà",
    "thế cũng đc", "cũng ổn á", "kó j đâu", "cũng đc mà", "haizz bt thui",
    "nói chung ổn", "tạm đc", "ko ý kiến", "học z cũng đc", "ờ học bt thôi",
    "chưa thấy j đặc biệt", "tạm thời ổn", "ko có j để nói", "vẫn bt như mọi khi",
    "kó j đáng nói", "okie thôi", "bình thường à", "vẫn thế thui", "ok nhe",
    "thôi cũng đc", "ừ học vậy cũng được", "bt quá mà", "chắc z thôi", "cũng ko tệ"
]

# Gán nhãn "1" = trung lập
neutral_data = [{"sentence": s, "sentiment": 1} for s in neutral_sentences]

# ====== Đọc dataset gốc nếu có ======
df = pd.read_csv(r"data_clean\feedback_train_clean.csv")   # nếu bạn đã có dữ liệu cũ

# ====== Ghép vào ======
df_neutral = pd.DataFrame(neutral_data)

# Nếu muốn mô phỏng khoảng 1000 câu, nhân bản + random hoán đổi câu
aug_neutral = []
for i in range(50):  # tạo 50 biến thể cho mỗi câu
    for s in neutral_sentences:
        variant = s.replace("ổn", random.choice(["ổn", "bình thường", "tạm được", "okie"]))
        variant = variant.replace("bài giảng", random.choice(["bài học", "tiết học", "giờ giảng"]))
        aug_neutral.append({"sentence": variant, "sentiment": 1})

df_aug = pd.DataFrame(aug_neutral)

# ====== Gộp & Lưu ======
df_final = pd.concat([df_neutral, df_aug], ignore_index=True)
df_final.to_csv("neutral_balanced.csv", index=False)

print("✅ Đã tạo file neutral_balanced.csv với", len(df_final), "mẫu trung lập.")
print(df_final.sample(5))
