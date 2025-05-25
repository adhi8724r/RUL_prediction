import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load('rul.pkl')  # replace with your actual model filename
#770.44	179.523810	3.773	3.742	922.775	1412.38	6678.88
#7393.76	1112.992000	4.249	3.224	5508.993	6762.02	10420.38
# UI title
st.title("🔋 Battery RUL Prediction")

st.write("Enter the following values to predict the Remaining Useful Life (RUL) of the battery:")

col1, col2 = st.columns(2)

with col1:
    discharge_time = st.number_input("Discharge Time (s)", min_value=0.0, value=7393.76)
with col2:
    decrement_voltage = st.number_input("Decrement 3.6-3.4V (s)", min_value=0.0, value=1112.992)

col3, col4 = st.columns(2)
with col3:
    max_voltage = st.number_input("Max. Voltage During Discharge (V)", min_value=0.0, value=4.249)
with col4:
    min_voltage = st.number_input("Min. Voltage During Charge (V)", min_value=0.0, value=3.224)

col5, col6 = st.columns(2)
with col5:
    time_at_4_15V = st.number_input("Time at 4.15V (s)", min_value=0.0, value=5508.993)
with col6:
    time_constant_current = st.number_input("Time at Constant Current (s)", min_value=0.0, value=6762.02)

# Last field on its own row (or pair with any other optional field)
col7, _ = st.columns(2)
with col7:
    charging_time = st.number_input("Charging Time (s)", min_value=0.0, value=10420.38)

# Predict button
if st.button("Predict RUL"):
    input_data = np.array([[discharge_time, decrement_voltage, max_voltage,
                            min_voltage, time_at_4_15V, time_constant_current, charging_time]])
    
    prediction = model.predict(input_data)
    st.success(f"🔧 Estimated RUL: **{prediction[0]:.2f} cycles**")