import streamlit as st
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Đường dẫn đến các pkl
model_path = 'D:\\Năm 4_HK1\\Phân tích Dữ liệu\\save\\svr.pkl'
scaler_path = 'D:\\Năm 4_HK1\\Phân tích Dữ liệu\\save\\scaler.pkl'
encoder_path = 'D:\\Năm 4_HK1\\Phân tích Dữ liệu\\save\\label_encoder.pkl'

# Load các file pkl
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)
label_encoders = joblib.load(encoder_path)

# Hàm xử lý dữ liệu đầu vào
def preprocess_input(data):

    selected_features = ['Attendance','Hours_Studied','Previous_Scores','Tutoring_Sessions','Peer_Influence','Distance_from_Home',
                           'Learning_Disabilities','Access_to_Resources','Parental_Involvement', 'Teacher_Quality']
    data_copy = data[selected_features].copy()

    categorical_features = ['Peer_Influence','Distance_from_Home', 'Learning_Disabilities',
                            'Access_to_Resources','Parental_Involvement', 'Teacher_Quality']

    columns_to_scale = ['Attendance', 'Hours_Studied', 'Previous_Scores', 'Tutoring_Sessions']

    for col in categorical_features:
        data_copy[col] = label_encoders[col].transform(data_copy[col])

    data_copy[columns_to_scale] = scaler.transform(data_copy[columns_to_scale])

    return data_copy


def main():

    # Cài đặt cấu hình ứng dụng
    st.set_page_config(
        page_title="Student Performance Factors",
        layout="wide"
    )

    # CSS cho màu sắc và giao diện
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #f0f8ff; /* Nền xanh nhạt */
            }
            .main-title {
                background-color: #00bfff; /* Màu xanh biển */
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
            }
            .sidebar .block-container {
                background-color: #e0f7fa; /* Nền xanh nhạt ở Sidebar */
                border-radius: 10px;
                padding: 10px;
            }
            .sidebar select, .sidebar input, .sidebar textarea {
                border-radius: 5px;
                border: 1px solid #00acc1;
            }
            .dataframe {
                border: 2px solid #00acc1;
                border-radius: 8px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Tiêu đề chính
    st.markdown('<h1 class="main-title">StudentPerformanceFactors</h1>', unsafe_allow_html=True)
    
    # Sidebar cho nhập thông tin từ người dùng
    st.sidebar.header('💡 Input Parameters')
    
    # Nhập các thông số từ người dùng
    hour_studied = st.sidebar.number_input('📚 Hour studied', value=0)
    attendance = st.sidebar.slider('🗓️ Attendance (%)', min_value=0, max_value=100, value=50)
    parental_involvement = st.sidebar.selectbox('👨‍👩‍👧‍👦 Parental involvement', ["Low", "Medium", "High"])
    access_to_resources = st.sidebar.selectbox('🔑 Access to resources', ["Low", "Medium", "High"])
    extracurricular_activities = st.sidebar.selectbox('🎭 Extracurricular activities', ['No', 'Yes'])
    sleep_hours = st.sidebar.number_input('🛌 Sleep hours', value=0)
    previous_scores = st.sidebar.slider('📊 Previous scores', min_value=0, max_value=100, value=50)
    motivation_level = st.sidebar.selectbox('🔥 Motivation level', ["Low", "Medium", "High"])
    internet_access = st.sidebar.selectbox('🌐 Internet access', ['No', 'Yes'])
    tutoring_sessions = st.sidebar.number_input('📘 Tutoring sessions', value=0)
    family_income = st.sidebar.selectbox('💰 Family income', ["Low", "Medium", "High"])
    teacher_quality = st.sidebar.selectbox('🧑‍🏫 Teacher Quality', ["Low", "Medium", "High"])
    school_type = st.sidebar.selectbox('🏫 School type', ["Public", "Private"])
    peer_influence = st.sidebar.selectbox('🤝 Peer influence', ["Positive", "Negative", "Neutral"])
    physical_activity = st.sidebar.number_input('🏃‍♂️ Physical activity', value=0)
    learning_disabilities = st.sidebar.selectbox('🧠 Learning disabilities', ['No', 'Yes'])
    parental_education_level = st.sidebar.selectbox('🎓 Parental education level', ['High School', 'College', 'Postgraduate'])
    distance_from_home = st.sidebar.selectbox('📍 Distance from home', ["Near", "Moderate", "Far"])
    gender = st.sidebar.selectbox('⚧️ Gender', ["Male", "Female"])

    # Tạo DataFrame từ thông tin nhập từ người dùng
    input_data = pd.DataFrame({
        'Hours_Studied': [hour_studied],
        'Attendance': [attendance],
        'Parental_Involvement': [parental_involvement],
        'Access_to_Resources': [access_to_resources],
        'Extracurricular_Activities': [extracurricular_activities],
        'Sleep_Hours': [sleep_hours],
        'Previous_Scores': [previous_scores],
        'Motivation_Level': [motivation_level],
        'Internet_Access': [internet_access],
        'Tutoring_Sessions': [tutoring_sessions],
        'Family_Income': [family_income],
        'Teacher_Quality': [teacher_quality],
        'School_Type': [school_type],
        'Peer_Influence': [peer_influence],
        'Physical_Activity': [physical_activity],
        'Learning_Disabilities': [learning_disabilities],
        'Parental_Education_Level': [parental_education_level],
        'Distance_from_Home': [distance_from_home],
        'Gender': [gender]
    })

    processed_data = preprocess_input(input_data)

    # Xử lý dữ liệu đầu vào và hiển thị kết quả
    if st.sidebar.button('Confirm Input Data'):
        st.subheader("📋 Input Data")
        st.write(input_data.style.set_properties(**{'background-color': '#f0f8ff', 'border-color': '#00acc1'}))

    if st.sidebar.button('Predict'):
        st.subheader("📋 Input Data")
        st.write(input_data.style.set_properties(**{'background-color': '#f0f8ff', 'border-color': '#00acc1'}))

        processed_data = preprocess_input(input_data)
        st.subheader("📋 Processed Data")
        st.write(processed_data.style.set_properties(**{'background-color': '#f0f8ff', 'border-color': '#00acc1'}))

        predictions = model.predict(processed_data)
        input_data['Exam_Score'] = predictions
        st.subheader("📋 Predicted Exam Score")
        exam_score_df = input_data[['Exam_Score']]
        st.write(exam_score_df.style.set_properties(**{'background-color': '#f0f8ff', 'border-color': '#00acc1'}))

# Chạy ứng dụng
if __name__ == '__main__':
    main()