import streamlit as st
import pandas as pd
import joblib

# 1. Саҳифа созламалари
st.set_page_config(page_title="Amazon Delivery Predictor", layout="wide")


# 2. Моделни юклаш
@st.cache_resource
def load_model():
    return joblib.load('amazon_delivery_model.pkl')


model = load_model()

# 3. Интерфейс сарлавҳаси
st.title("📦 Amazon Delivery Time Predictor")
st.markdown("Ушбу илова AI ёрдамида етказиб бериш вақтини башорат қилади.")

# 4. Киритиш майдонларини икки устунга бўламиз
col1, col2 = st.columns(2)

with col1:
    st.header("👤 Курьер ва Ҳудуд")
    agent_age = st.slider("Курьер ёши", 18, 60, 30)
    agent_rating = st.slider("Курьер рейтинги", 1.0, 5.0, 4.5, 0.1)
    area = st.selectbox("Ҳудуд тури", ['Metropolitian', 'Urban', 'Semi-Urban'])
    category = st.selectbox("Товар тоифаси", ['Food', 'Electronics', 'Clothing', 'Groceries', 'Appliances'])

with col2:
    st.header("🚚 Етказиб бериш деталлари")
    distance = st.number_input("Масофа (км)", min_value=1.0, max_value=50.0, value=10.0)
    traffic = st.select_slider("Тирбандлик", options=['Low', 'Medium', 'High', 'Jam'])
    weather = st.selectbox("Об-ҳаво", ['Sunny', 'Cloudy', 'Windy', 'Sandstorms', 'Stormy', 'Fog'])
    vehicle = st.selectbox("Транспорт", ['Motorcycle', 'Scooter', 'Electric_Bike', 'Bicycle'])
    hour = st.slider("Буюртма вақти (соат)", 0, 23, 14)
    day = st.slider("Ҳафта куни (0=Душ, 6=Якш)", 0, 6, 2)

# 5. Башорат қилиш тугмаси
if st.button("Вақтни ҳисоблаш"):
    # Маълумотларни DataFrame кўринишига келтирамиз
    input_df = pd.DataFrame([{
        'Agent_Age': agent_age,
        'Agent_Rating': agent_rating,
        'distance_km': distance,
        'Traffic': traffic,
        'Weather': weather,
        'Vehicle': vehicle,
        'Area': area,
        'Category': category,
        'order_hour': hour,
        'day_of_week': day
    }])

    # Башорат
    prediction = model.predict(input_df)[0]

    # Натижани чиқариш
    st.success(f"🔥 Тахминий етказиб бериш вақти: **{prediction:.2f} дақиқа**")

    # Қўшимча мантиқий маълумот
    st.info(f"Бу тахминан **{int(prediction // 60)} соат {int(prediction % 60)} дақиқа** демакдир.")