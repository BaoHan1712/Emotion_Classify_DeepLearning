import matplotlib.pyplot as plt

# ======= DỮ LIỆU =======

labels = ["Tiêu cực", "Trung lập", "Tích cực"]
colors = ["#ff4d4d", "#ffd11a", "#66b3ff"]

# ======= VẼ BIỂU ĐỒ HÌNH TRÒN =======
total_values = [11426+1583+3166, 5325+705+1409, 458+73+167]

plt.figure(figsize=(6,6))
plt.pie(total_values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90, textprops={'fontsize': 12})
plt.title("Phân bố cảm xúc toàn bộ dữ liệu", fontsize=14, fontweight="bold")
plt.show()
