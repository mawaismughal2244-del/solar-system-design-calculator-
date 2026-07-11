import streamlit as st

st.set_page_config(page_title="Solar System Design Calculator", page_icon="â˜€ï¸")

st.title("â˜€ï¸ Solar System Design Calculator")

load = st.number_input("Total Load (W)", min_value=0.0)
hours = st.number_input("Usage Hours / Day", min_value=0.0, value=5.0)
sun = st.number_input("Peak Sun Hours", min_value=1.0, value=5.0)
panel_brand = st.selectbox("Panel Brand",["Longi","Jinko","JA Solar","Canadian Solar","Trina"])
panel_watt = st.selectbox("Panel Wattage",[450,550,585,610])
inv_brand = st.selectbox("Inverter Brand",["Growatt","GoodWe","Inverex","Fronus","Knox","Crown"])
inv_type = st.selectbox("Inverter Type",["Hybrid","On Grid","Off Grid"])
bat_type = st.selectbox("Battery Type",["Lithium LiFePO4","Tubular","AGM","Gel"])
bat_brand = st.selectbox("Battery Brand",["BYD","Pylontech","Narada","AGS","Phoenix"])
voltage = st.selectbox("Battery Voltage",[12,24,48])
backup = st.number_input("Backup Hours", min_value=1.0, value=4.0)
unit_price = st.number_input("Electricity Price (PKR/unit)", value=65.0)

if st.button("Calculate"):
    daily = load*hours
    solar = daily/sun if sun else 0
    panels = int(-(-solar//panel_watt))
    battery_ah = (daily*backup)/voltage
    inverter = load*1.25
    cost = (solar/1000)*140000
    monthly_units = daily*30/1000
    monthly_save = monthly_units*unit_price
    yearly_save = monthly_save*12

    st.subheader("System Report")
    st.write(f"**Panel Brand:** {panel_brand}")
    st.write(f"**Panels Required:** {panels}")
    st.write(f"**Required Solar Size:** {solar:.1f} W")
    st.write(f"**Inverter:** {inv_brand} ({inv_type})")
    st.write(f"**Recommended Inverter Size:** {inverter:.1f} W")
    st.write(f"**Battery:** {bat_brand} - {bat_type}")
    st.write(f"**Battery Capacity:** {battery_ah:.1f} Ah")
    st.write(f"**Estimated System Cost:** PKR {cost:,.0f}")
    st.write(f"**Estimated Monthly Saving:** PKR {monthly_save:,.0f}")
    st.write(f"**Estimated Yearly Saving:** PKR {yearly_save:,.0f}")

