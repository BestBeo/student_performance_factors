# Dự Án Dự Đoán Điểm Thi Dựa Trên Các Yếu Tố Ảnh Hưởng Đến Hiệu Suất Học Tập

## Tổng quan
Dự án **Student Performance Factors** tập trung vào việc phân tích và dự đoán điểm thi cuối kỳ của học sinh dựa trên các yếu tố ảnh hưởng đến hiệu suất học tập. Dự án sử dụng tập dữ liệu `StudentPerformanceFactors.csv`, bao gồm các yếu tố học thuật và phi học thuật như số giờ học, tỷ lệ tham gia lớp học, sự tham gia của phụ huynh, và các yếu tố khác. Mô hình máy học được sử dụng là **SVR (Support Vector Regression)** với các tham số được tối ưu hóa thông qua GridSearchCV, đạt R-squared (R2) là 0.6417 trên tập kiểm tra.

Dự án bao gồm hai thành phần chính:
- **Notebook huấn luyện mô hình** (`StudentPerformanceFactors_full.ipynb`): Xử lý dữ liệu, huấn luyện mô hình SVR, và lưu các thành phần cần thiết (mô hình, scaler, label encoder) dưới dạng tệp `.pkl`.
- **Ứng dụng Streamlit** (`ptdl.py`): Cung cấp giao diện người dùng để nhập thông tin học sinh và dự đoán điểm thi dựa trên mô hình đã huấn luyện.

Mục tiêu của dự án là hỗ trợ giáo viên, phụ huynh và nhà giáo dục trong việc xác định các yếu tố quan trọng ảnh hưởng đến kết quả học tập, từ đó đưa ra các chiến lược hỗ trợ hiệu quả hơn.

## Tính năng
- **Phân tích dữ liệu**: Khám phá các yếu tố ảnh hưởng đến điểm thi thông qua tập dữ liệu `StudentPerformanceFactors.csv`.
- **Huấn luyện mô hình**: Sử dụng mô hình SVR với các tham số tối ưu (`C=10`, `epsilon=0.2`, `gamma='scale'`, `kernel='rbf'`) để dự đoán điểm thi.
- **Ứng dụng dự đoán**: Một giao diện Streamlit thân thiện cho phép người dùng nhập thông tin học sinh và nhận kết quả dự đoán điểm thi.
- **Tiền xử lý dữ liệu**: Chuyển đổi các đặc trưng phân loại thành số (LabelEncoder) và chuẩn hóa các đặc trưng số (StandardScaler).
- **Hiệu suất cao**: Mô hình SVR đạt các chỉ số:
  - Mean Absolute Error (MAE): 0.8966
  - Mean Squared Error (MSE): 5.4460
  - R-squared (R2): 0.6418

## Tập dữ liệu
Tập dữ liệu `StudentPerformanceFactors.csv` bao gồm 20 cột, đại diện cho các yếu tố ảnh hưởng đến hiệu suất học tập của học sinh:
- **Hours_Studied**: Số giờ học mỗi tuần.
- **Attendance**: Tỷ lệ phần trăm tham gia lớp học.
- **Parental_Involvement**: Mức độ tham gia của phụ huynh (Low, Medium, High).
- **Access_to_Resources**: Tính khả dụng của tài nguyên giáo dục (Low, Medium, High).
- **Extracurricular_Activities**: Tham gia hoạt động ngoại khóa (Yes, No).
- **Sleep_Hours**: Số giờ ngủ trung bình mỗi đêm.
- **Previous_Scores**: Điểm số từ các kỳ thi trước.
- **Motivation_Level**: Mức độ động lực (Low, Medium, High).
- **Internet_Access**: Tính khả dụng của internet (Yes, No).
- **Tutoring_Sessions**: Số buổi học kèm mỗi tháng.
- **Family_Income**: Thu nhập gia đình (Low, Medium, High).
- **Teacher_Quality**: Chất lượng giáo viên (Low, Medium, High).
- **School_Type**: Loại trường (Public, Private).
- **Peer_Influence**: Ảnh hưởng của bạn bè (Positive, Neutral, Negative).
- **Physical_Activity**: Số giờ hoạt động thể chất mỗi tuần.
- **Learning_Disabilities**: Có khuyết tật học tập không (Yes, No).
- **Parental_Education_Level**: Trình độ học vấn của phụ huynh (High School, College, Postgraduate).
- **Distance_from_Home**: Khoảng cách từ nhà đến trường (Near, Moderate, Far).
- **Gender**: Giới tính (Male, Female).
- **Exam_Score**: Điểm thi cuối kỳ (biến mục tiêu).

Mô hình chỉ sử dụng 10 đặc trưng quan trọng nhất: `Attendance`, `Hours_Studied`, `Previous_Scores`, `Tutoring_Sessions`, `Peer_Influence`, `Distance_from_Home`, `Learning_Disabilities`, `Access_to_Resources`, `Parental_Involvement`, `Teacher_Quality`.

## Yêu cầu
Để chạy dự án này, bạn cần cài đặt các gói phụ thuộc sau:
- Python 3.6 trở lên
- pandas
- scikit-learn
- joblib
- streamlit

Bạn có thể cài đặt các gói cần thiết bằng cách sử dụng tệp `requirements.txt` (xem phần Cài đặt bên dưới).

Ngoài ra, bạn cần:
- Tệp mô hình đã huấn luyện (`svr.pkl`), scaler (`scaler.pkl`), và label encoder (`label_encoder.pkl`), được đặt trong thư mục `save/`.
- Tệp dữ liệu `StudentPerformanceFactors.csv` để huấn luyện mô hình (nếu cần).

## Cài đặt
1. **Tải kho lưu trữ**:
   ```bash
   git clone https://github.com/BestBeo/student_performance_factors.git
   cd student_performance_factors
   ```

2. **Thiết lập môi trường và cài đặt phụ thuộc**:
   Tạo một môi trường ảo (khuyến nghị) và cài đặt các gói từ `requirements.txt`:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Thiết lập cấu trúc thư mục**:
   Đảm bảo bạn có cấu trúc thư mục sau:
   ```
   student_performance_factors/
   ├── data/
   │   └── StudentPerformanceFactors.csv
   ├── save/
   │   ├── svr.pkl
   │   ├── scaler.pkl
   │   └── label_encoder.pkl
   ├── ptdl.py
   ├── StudentPerformanceFactors_full.ipynb
   └── requirements.txt
   ```

4. **Tải mô hình và tệp liên quan**:
   - Đảm bảo các tệp `svr.pkl`, `scaler.pkl`, và `label_encoder.pkl` nằm trong thư mục `save/`. Các tệp này được tạo ra sau khi chạy notebook `StudentPerformanceFactors_full.ipynb`.
   - Nếu bạn cần huấn luyện lại mô hình, đặt tệp `StudentPerformanceFactors.csv` vào thư mục `data/`.

## Sử dụng
### Huấn luyện mô hình
Để huấn luyện mô hình SVR và lưu các tệp cần thiết:
1. Mở notebook `StudentPerformanceFactors_full.ipynb` trong môi trường Jupyter (ví dụ: Google Colab hoặc Jupyter Notebook).
2. Đảm bảo tệp `StudentPerformanceFactors.csv` có thể truy cập trong thư mục `data/` (hoặc điều chỉnh đường dẫn trong notebook nếu cần).
3. Chạy các ô trong notebook để:
   - Tải và tiền xử lý dữ liệu.
   - Chọn các đặc trưng quan trọng.
   - Chuẩn hóa dữ liệu (StandardScaler) và mã hóa các đặc trưng phân loại (LabelEncoder).
   - Tối ưu hóa tham số cho mô hình SVR bằng GridSearchCV.
   - Lưu mô hình (`svr.pkl`), scaler (`scaler.pkl`), và label encoder (`label_encoder.pkl`) vào thư mục `save/`.
4. Kết quả huấn luyện sẽ hiển thị các chỉ số hiệu suất (MAE, MSE, R2).

### Dự đoán điểm thi bằng ứng dụng Streamlit
Để chạy ứng dụng Streamlit và dự đoán điểm thi:
1. Đảm bảo các tệp `svr.pkl`, `scaler.pkl`, và `label_encoder.pkl` nằm trong thư mục `save/`.
2. Chạy tệp `ptdl.py` bằng lệnh:
   ```bash
   streamlit run ptdl.py
   ```
3. Một giao diện web sẽ mở ra trong trình duyệt của bạn. Trong giao diện:
   - Nhập các thông số của học sinh thông qua sidebar (ví dụ: số giờ học, tỷ lệ tham gia lớp, mức độ tham gia của phụ huynh, v.v.).
   - Nhấn nút **Confirm Input Data** để xem dữ liệu đầu vào.
   - Nhấn nút **Predict** để xem dữ liệu đã xử lý và điểm thi dự đoán (`Exam_Score`).

### Đầu ra
- **Dữ liệu đầu vào**: Hiển thị thông tin học sinh đã nhập.
- **Dữ liệu đã xử lý**: Hiển thị dữ liệu sau khi được tiền xử lý (mã hóa và chuẩn hóa).
- **Điểm thi dự đoán**: Hiển thị điểm thi cuối kỳ (`Exam_Score`) được dự đoán bởi mô hình SVR.

## Mô tả các tệp
- **`ptdl.py`**: Ứng dụng Streamlit để nhập thông tin học sinh và dự đoán điểm thi. Tệp này tải mô hình SVR, scaler, và label encoder từ thư mục `save/`, sau đó tiền xử lý dữ liệu đầu vào và đưa ra dự đoán.
- **`StudentPerformanceFactors_full.ipynb`**: Notebook Jupyter để phân tích dữ liệu, huấn luyện mô hình SVR, và lưu các tệp `.pkl`. Notebook cũng bao gồm bước tối ưu hóa tham số bằng GridSearchCV.
- **`requirements.txt`**: Liệt kê các thư viện Python cần thiết để chạy dự án.
- **`data/StudentPerformanceFactors.csv`**: Tệp dữ liệu chứa thông tin về các yếu tố ảnh hưởng đến hiệu suất học tập.
- **`save/`**: Thư mục chứa các tệp đã lưu:
  - `svr.pkl`: Mô hình SVR đã huấn luyện.
  - `scaler.pkl`: StandardScaler đã được fit trên dữ liệu huấn luyện.
  - `label_encoder.pkl`: Từ điển các LabelEncoder cho các đặc trưng phân loại.

## Hiệu suất mô hình
Mô hình SVR đã được tối ưu hóa đạt các chỉ số sau trên tập kiểm tra:
- **Mean Absolute Error (MAE)**: 0.8966
- **Mean Squared Error (MSE)**: 5.4460
- **R-squared (R2)**: 0.6418

Các tham số tối ưu của mô hình:
- `C`: 10
- `epsilon`: 0.2
- `gamma`: 'scale'
- `kernel`: 'rbf'

## Hạn chế
- **Phụ thuộc vào dữ liệu huấn luyện**: Hiệu suất mô hình phụ thuộc vào chất lượng và độ đa dạng của tập dữ liệu `StudentPerformanceFactors.csv`.
- **Đặc trưng hạn chế**: Mô hình chỉ sử dụng 10 đặc trưng quan trọng nhất, có thể bỏ qua các yếu tố khác có ảnh hưởng nhỏ.
- **Hiệu suất dự đoán**: Với R2 là 0.6418, mô hình có thể không dự đoán chính xác trong một số trường hợp phức tạp.
- **Môi trường chạy**: Ứng dụng Streamlit yêu cầu các tệp `.pkl` phải nằm đúng vị trí, nếu không sẽ gây lỗi.

## Cải tiến trong tương lai
- Sử dụng các mô hình phức tạp hơn (ví dụ: Neural Networks) để cải thiện độ chính xác dự đoán.
- Mở rộng tập dữ liệu để bao gồm nhiều yếu tố và mẫu dữ liệu hơn.
- Thêm chức năng phân tích sâu hơn trong ứng dụng Streamlit, ví dụ: hiển thị tầm quan trọng của các đặc trưng.
- Tối ưu hóa giao diện Streamlit để thân thiện hơn với người dùng.

## Đóng góp
Chúng tôi hoan nghênh mọi đóng góp! Vui lòng fork kho lưu trữ, thực hiện thay đổi và gửi pull request. Đảm bảo rằng mã mới tuân theo cấu trúc hiện có và bao gồm tài liệu phù hợp.

## Giấy phép
Dự án này được cấp phép theo Giấy phép MIT. Xem tệp [LICENSE](LICENSE) để biết chi tiết.

## Lời cảm ơn
- Tập dữ liệu được lấy từ nguồn công khai và sử dụng cho mục đích học tập.
- Cảm ơn cộng đồng mã nguồn mở vì đã cung cấp các thư viện như pandas, scikit-learn, và Streamlit.

## Liên hệ
Nếu có câu hỏi hoặc vấn đề, vui lòng mở một issue trên [kho lưu trữ GitHub](https://github.com/BestBeo/student_performance_factors) hoặc liên hệ với người duy trì dự án.
