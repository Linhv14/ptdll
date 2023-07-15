# Hướng dẫn
## Bước 1: Xuất model dự đoán

Sau khi chọn được model. Giả sử model là LinearRegression
```
model = LinearRegression()
```

Sau khi train xong ta sẽ xuất model ra bằng cách

```
import joblib

# Lưu mô hình thành tệp joblib
joblib.dump(model, 'modelname.joblib')
```
Nếu chạy bằng google colab thì file model sẽ xuất hiện ở tab chung với
gg drive. Tải file model về

## Bước 2: Cài đặt code

Cần để model và file code chung 1 thư mục
Sau đó mở file code, tải các thư viện cần thiết
ví dụ nếu chưa có sklearn, gõ trên terminal lệnh
```
pip install sklearn
```

Đối với file code. Cần đảm bảo tên cột trong model train giống với tên
cột dự đoán trong file code
ví dụ trong file code `store.py` có đoạn code sau:
```
data = pd.DataFrame([[stores]], columns=['n_store'])
```

Nếu cột đầu vào có tên là `number of stores in district` thì cần sửa lại
```
data = pd.DataFrame([[stores]], columns=['number of stores in district'])
```

## Bước 3: Điều chỉnh tham số file system
Ở đoạn code sau:
```
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```

Nếu build ứng dụng ra exe và chạy thử, ứng dụng báo lỗi `FileNotFound` gì đó thì có thể điều chỉnh `_MEIPASS2` thành `_MEIPASS`

# Bước 4: Build thành file exe

Mở terminal, đảm bảo rằng đường dẫn đang trỏ đúng tới thư mục chứ code và model.
Đầu tiên chạy lệnh sau trên terminal
```
pip install pyinstaller
```
Sau đó chạy lệnh
```
pyinstaller --onefile store.py
```
store.py chính là tên file code, nếu tên file code đặt tên khác thì
chỉnh lại

Sau khi build xong, sẽ xuất hiện thư mục dist, lúc này cần copy file model và past vào trong thư mục dist.

Click vào file exe để chạy. Nếu chạy không xuất hiện lỗi thì có thể quay lại termianl chạy lệnh cuối cùng sau:
```
pyinstaller --onefile -w store.py
```

Lúc build ra, khi chạy ứng dụng sẽ không còn thấy terminal bật lên nữa

### Đối với bài toán titanic
Đầu vào chỉ có 5 cột:
```
  data = {
    'Pclass': [pclass],
    'Age': [age],
    'Fare': [fare],
    'Gender_Encoded': [gender],
    'Familiars': [familiars]
  }
```

Nếu mô hình có nhiều hoặc ít hơn, hãy tự tạo thêm input hoặc xóa bớt cho phù hợp. Lưu ý cầ đảm bảo tên cột trong file code này tương ứng với tên cột đã train model.
