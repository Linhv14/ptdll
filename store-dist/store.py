import tkinter as tk
import pandas as pd
import joblib
import os
import sys
import sklearn
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def validate_input(input_text):
  if input_text.isdigit():
    return True
  elif input_text == "":
    return True
  else:
    return False

def clear_input():
    input_entry.delete(0, tk.END)

def predict():
  stores = input_entry.get()

  model_path = resource_path("store.joblib")
  # Load model
  model = joblib.load(model_path)
  data = pd.DataFrame([[stores]], columns=['n_store'])
  sales = model.predict(data)[0]
  rounded_sales = round(sales, 2)

  result_label.config(text=f"Với {stores} cửa hàng, doanh thu dự đoán là: {rounded_sales}")
  clear_input()

window = tk.Tk()
window.title("Dự đoán doanh thu")
# Thiết lập cấu trúc lưới
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Đặt kích thước cửa sổ
window.geometry("400x120")

# Tạo một hàm kiểm tra kiểu số
validate_number = window.register(validate_input)

# Nhãn để nhập
input_label = tk.Label(window, text="Nhập số lượng cửa hàng")
input_label.grid(row=0, column=0, columnspan=2)


# Tạo ô đầu vào chỉ cho phép nhập số
input_entry = tk.Entry(window, validate="key", validatecommand=(validate_number, '%P'))
input_entry.configure(bg="#F0F0F0")
input_entry.grid(row=1, column=0, padx=12, pady=12, sticky="ew")

# Hàm xử lý sự kiện khi nhấp vào nút dự đoán
predict_button = tk.Button(window, text="Dự đoán", command=predict)
predict_button.grid(row=1, column=1, padx=12, pady=12)
predict_button.config(bg="#ff6e40", fg="white")

# Nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=12)

window.mainloop()