import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="EV App")

st.title("🚗 EV Battery & Charging App")

# Tabs
tab1, tab2 = st.tabs(["🔋 Battery Health", "⚡ Charging Simulator"])

# -----------------------
# Battery Health
# -----------------------
with tab1:
    st.header("Battery Health Predictor")

    cycles = st.slider("Charge Cycles", 0, 2000, 500)
    temp = st.slider("Temperature (°C)", 20, 60, 30)
    dod = st.slider("Depth of Discharge (%)", 20, 100, 80)

    health = 100 - (cycles * 0.02 + temp * 0.3 + dod * 0.1)
    health = max(0, round(health, 2))

    st.metric("Battery Health (%)", health)

    if health > 80:
        st.success("Good Condition ✅")
    elif health > 50:
        st.warning("Moderate Condition ⚠️")
    else:
        st.error("Poor Battery ❌")

# -----------------------
# Charging Simulator
# -----------------------
with tab2:
    st.header("EV Charging Simulator")

    capacity = st.slider("Battery Capacity (kWh)", 20, 100, 60)
    power = st.slider("Charger Power (kW)", 3, 50, 10)
    soc = st.slider("Initial Charge (%)", 0, 100, 20)

    time = (capacity * (100 - soc) / 100) / power

    st.write(f"Charging Time: {round(time, 2)} hours")

    t = np.linspace(0, time, 100)
    soc_curve = soc + (100 - soc) * (1 - np.exp(-t / time))

    fig = px.line(x=t, y=soc_curve, labels={"x": "Time", "y": "SOC (%)"})
    st.plotly_chart(fig)