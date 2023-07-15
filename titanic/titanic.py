import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib
import os
import sys
import sklearn
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def validate_float(input_value):
    try:
        if input_value == "":
          return True
        float(input_value)
        return True
    except ValueError:
        return False


def validate_int(input_text):
  if input_text.isdigit():
    return True
  elif input_text == "":
    return True
  else:
    return False


def clear_input():
  input_age_entry.delete(0, tk.END)
  input_familiars_entry.delete(0, tk.END)
  input_fare_entry.delete(0, tk.END)
  option_pclass_combobox.set(pclass_options[0])
  option_gender_combobox.set(gender_options[0])

def extract_gender(gender):
  if gender == gender_options[0]:
    return 1
  else:
    return 2

def extract_survived(is_survived):
  if is_survived == 0:
    return "Không sống sót"
  else:
    return "Sống sót"

def predict():
  required_value = [input_age_entry.get(), input_familiars_entry.get(), input_fare_entry.get()]
  if "" in required_value: 
    return

  age = float(input_age_entry.get())
  pclass = float(option_pclass_combobox.get())
  familiars = int(input_familiars_entry.get())
  gender = int(extract_gender(option_gender_combobox.get()))
  fare = float(input_fare_entry.get())

  model_path = resource_path("titanic.joblib")
  # Load model
  model = joblib.load(model_path)

  data = {
    'Pclass': [pclass],
    'Age': [age],
    'Fare': [fare],
    'Gender_Encoded': [gender],
    'Familiars': [familiars]
  }

  passenger = pd.DataFrame(data)
  is_survived = model.predict(passenger)

  result = extract_survived(is_survived)
  result_label.config(text=f"Survived: {result}")

  clear_input()

window = tk.Tk()
window.title("Dự đoán sinh tồn trong chuyến tàu Titanic")
# Thiết lập cấu trúc lưới
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
# Đặt kích thước cửa sổ
window.geometry("400x440")


# Option các hạng ghế
pclass_options = ["1", "2", "3"]

# Nhãn để hiển thị kết quả
pclass_label = tk.Label(window, text="Hạng ghế | Pclass")
pclass_label.grid(row=0, column=0, sticky="ew")
# Tạo widget Combobox
option_pclass_combobox = ttk.Combobox(window, values=pclass_options, state='readonly')
option_pclass_combobox.set(pclass_options[0])  
option_pclass_combobox.grid(row=1, column=0, padx=12, pady=12, sticky="ew")


age_label = tk.Label(window, text="Tuổi | Age")
age_label.grid(row=2, column=0, sticky="ew")


# Tạo một hàm kiểm tra kiểu float
validate_float_number = window.register(validate_float)

input_age_entry = tk.Entry(window, validate="key", validatecommand=(validate_float_number, '%P'))
input_age_entry.grid(row=3, column=0, padx=12, pady=12, sticky="ew")


# Option các giới tính
gender_options = ["Name | Male", "Nữ | Female"]

# Nhãn để hiển thị kết quả
gender_label = tk.Label(window, text="Giới tính | Gender")
gender_label.grid(row=4, column=0, sticky="ew")
# Tạo widget Combobox
option_gender_combobox = ttk.Combobox(window, values=gender_options, state='readonly')
option_gender_combobox.set(gender_options[0])  
option_gender_combobox.grid(row=5, column=0, padx=12, pady=12, sticky="ew")

fare_label = tk.Label(window, text="Giá vé | Fare")
fare_label.grid(row=6, column=0, sticky="ew")

input_fare_entry = tk.Entry(window, validate="key", validatecommand=(validate_float_number, '%P'))
input_fare_entry.grid(row=7, column=0, padx=12, pady=12, sticky="ew")


familiars_label = tk.Label(window, text="Số lượng người thân trên tàu | Familiars")
familiars_label.grid(row=8, column=0, sticky="ew")

# Tạo một hàm kiểm tra kiểu số
validate_int_number = window.register(validate_int)
input_familiars_entry = tk.Entry(window, validate="key", validatecommand=(validate_int_number, '%P'))
input_familiars_entry.grid(row=9, column=0, padx=12, pady=12, sticky="ew")


# Hàm xử lý sự kiện khi nhấp vào nút dự đoán
predict_button = tk.Button(window, text="Dự đoán", command=predict)
predict_button.grid(row=10, column=0, padx=12, pady=12, sticky="ew")
predict_button.config(bg="#ff6e40", fg="white")

# Nhãn để hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=11, column=0, columnspan=2, pady=12)

# Đặt chỉ số tab một cách rõ ràng
# Đặt chỉ số tab
window.tk.call('tk_focusNext', option_pclass_combobox)
window.tk.call('tk_focusNext', input_age_entry)
window.tk.call('tk_focusNext', option_gender_combobox)
window.tk.call('tk_focusNext', input_fare_entry)
window.tk.call('tk_focusNext', input_familiars_entry)
window.tk.call('tk_focusNext', predict_button)

window.mainloop()