import streamlit as st
import numpy as np
import pickle

@st.cache_resource
def load_model():
    with open("random_forest_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

import streamlit as st

st.title("Battery RUL Predictor")

# Layout with two columns per row
col1, col2 = st.columns(2)

with col1:
    initial_capacity = st.number_input("Initial Capacity (Ah)", min_value=0.0, value=1.8)

with col2:
    capacity = st.number_input("Current Capacity (Ah)", min_value=0.0, value=1.73)

col3, col4 = st.columns(2)

with col3:
    charge_time = st.number_input("Charge Time (s)", min_value=0, value=4500)

with col4:
    min_voltage_charge = st.number_input("Min Voltage During Charge (V)", min_value=0.0, value=2.2)

col5, col6 = st.columns(2)

with col5:
    discharge_time = st.number_input("Discharge Time (s)", min_value=0, value=5800)

with col6:
    max_voltage_discharge = st.number_input("Max Voltage During Discharge (V)", min_value=0.0, value=4.2)


battery_id_encoded = 1
cycle = st.number_input("Cycle Count", min_value=0, value=45)

# Auto-calculated features
total_time = charge_time + discharge_time
current_capacity_percent = (capacity / initial_capacity) * 100 if initial_capacity else 0
battery_fading_percent = 100 - current_capacity_percent

if st.button("Predict RUL"):
    input_data = np.array([[
        battery_id_encoded,
        initial_capacity,
        capacity,
        current_capacity_percent,
        battery_fading_percent,
        cycle,
        charge_time,
        min_voltage_charge,
        discharge_time,
        max_voltage_discharge,
        total_time
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"✅ Estimated RUL: **{prediction:.2f} cycles**")

    with st.expander("📊 Feature Summary"):
        st.write(f"**Total Time:** {total_time:.2f} s")
        st.write(f"**Current Capacity %:** {current_capacity_percent:.2f}%")
        st.write(f"**Battery Fading %:** {battery_fading_percent:.2f}%")
