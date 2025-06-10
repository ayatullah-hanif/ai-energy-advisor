import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="SolarPeer Advisor – Smart Energy & Cost Planner", layout="wide")
st.title("💡 SolarPeer Advisor – Smart Energy & Cost Planner")

# --- Load appliance data ---
@st.cache_data
def load_data():
    return pd.read_csv("appliance_power_ratings.csv")

# --- Tips generator ---
def get_advice(energy_kwh, cost, cheapest_source):
    tips = []
    if cheapest_source != "Solar":
        if energy_kwh > 150:
            tips.append("📉 Try reducing usage hours or appliance count for high-watt devices.")
        if cost > 10000:
            tips.append("🔁 Switch to inverter-based or solar appliances for long-term savings.")
        if cheapest_source == "NEPA":
            tips.append("⚡ NEPA is cheaper now, but use off-peak hours to avoid sudden costs.")
        if cheapest_source == "Generator":
            tips.append("⛽ Generators are expensive. Avoid running heavy appliances on them.")
        if not tips:
            tips.append("✅ Your energy setup is decent, but a few tweaks could reduce costs more.")
    return tips

appliance_df = load_data()

# --- Appliance selection ---
st.markdown("### 🔌 1. Select Appliances & Input Usage")
st.divider()
selected_appliances = st.multiselect("Choose appliances to analyze:", options=appliance_df["Appliance"].tolist())

appliance_inputs = []
if selected_appliances:
    st.markdown("#### 🔧 Appliance Usage Details")
    for appliance in selected_appliances:
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(f"{appliance} - Quantity", min_value=1, value=1, step=1, key=f"{appliance}_qty")
        with col2:
            hours = st.number_input(f"{appliance} - Daily Hours Used", min_value=0.0, value=1.0, step=0.5, key=f"{appliance}_hrs")
        watt = appliance_df[appliance_df["Appliance"] == appliance]["Power (Watts)"].values[0]
        appliance_inputs.append({
            "Appliance": appliance,
            "Quantity": quantity,
            "Hours_per_day": hours,
            "Power (Watts)": watt
        })

    # --- Data Calculation ---
    usage_df = pd.DataFrame(appliance_inputs)
    usage_df["Daily_Wh"] = usage_df["Quantity"] * usage_df["Hours_per_day"] * usage_df["Power (Watts)"]
    usage_df["Monthly_kWh"] = usage_df["Daily_Wh"] * 30 / 1000

    st.markdown("#### 📊 Estimated Monthly Usage")
    st.dataframe(usage_df[["Appliance", "Quantity", "Hours_per_day", "Power (Watts)", "Monthly_kWh"]], use_container_width=True)

    # --- Cost Estimation ---
    st.markdown("### 💰 2. Cost Estimation by Power Source")
    st.divider()
    NEPA_rate = 68
    GEN_cost = 150
    SOLAR_cost = 20

    total_kWh = usage_df["Monthly_kWh"].sum()
    cost_df = pd.DataFrame({
        "Source": ["NEPA", "Generator", "Solar"],
        "Cost_per_kWh": [NEPA_rate, GEN_cost, SOLAR_cost],
        "Estimated_Cost": [total_kWh * NEPA_rate, total_kWh * GEN_cost, total_kWh * SOLAR_cost]
    })

    st.dataframe(cost_df.set_index("Source"), use_container_width=True)

    cheapest = cost_df.loc[cost_df["Estimated_Cost"].idxmin()]["Source"]

    if cheapest == "Solar":
        st.success("✅ Solar appears to be the most cost-effective option for your usage.")
    else:
        st.warning(f"💸 {cheapest} is currently the most cost-effective.")
        tips = get_advice(total_kWh, cost_df["Estimated_Cost"].max(), cheapest)
        with st.expander("💡 Energy-Saving Advice"):
            for tip in tips:
                st.markdown(f"- {tip}")

    # --- SolarPeer360 Smart Plan ---
    st.markdown("### 🧠 3. SolarPeer360 Smart Plan")
    st.divider()

    if "solarpeer_active" not in st.session_state:
        st.session_state.solarpeer_active = False
        
    if st.button("Activate SolarPeer360 Smart Plan"):
        st.session_state.solarpeer_active = True
        
    if st.session_state.solarpeer_active:
        st.markdown("#### 🧍‍♂️ Tenant Optimization Mode")

        num_users = st.slider("How many users/tenants?", min_value=1, max_value=5, value=2)
        tenant_data = []

        for i in range(num_users):
            st.markdown(f"**User {i+1}**")
            selected = st.multiselect(f"Select appliances for User {i+1}", selected_appliances, key=f"user{i}_apps")
            sub_df = usage_df[usage_df["Appliance"].isin(selected)]
            user_kWh = sub_df["Monthly_kWh"].sum()
            user_cost = user_kWh * SOLAR_cost
            tenant_data.append((f"User {i+1}", user_kWh, user_cost))

        tenant_df = pd.DataFrame(tenant_data, columns=["User", "Monthly_kWh", "Estimated_Solar_Cost"])
        st.dataframe(tenant_df, use_container_width=True)

        st.markdown("### 📅 Smart Load Scheduling Tips")
        st.info("💡 Run high-power appliances like washing machines between 11am–3pm for best solar utilization.")

        st.markdown("### 🔋 Backup Source Advisor")
        st.warning("⚠️ Avoid using generators for heaters or irons – they are expensive! Use NEPA during off-peak if needed.")

        # Pie chart
        st.markdown("### 📈 Appliance Energy Distribution")
        colors = plt.cm.tab20.colors
        fig, ax = plt.subplots(figsize=(1, 1))
        fig.patch.set_alpha(0)
        ax.set_facecolor("none")
        wedges,_ = ax.pie(usage_df["Monthly_kWh"], startangle=90, colors=colors[:len(usage_df)], radius=1)
        ax.axis("equal")
        col1, col2 = st.columns([1, 1])

        with col1:
            st.pyplot(fig)

        with col2:
            labels = usage_df["Appliance"].values
            values = usage_df["Monthly_kWh"].round(2).values
            color_list = colors[:len(labels)]

            legend_df = pd.DataFrame({
                "Appliance": labels,
                "Monthly_kWh": values
            })
            color_styles = [
                f"background-color: rgba({int(r*255)}, {int(g*255)}, {int(b*255)}, 0.85)"
                for r, g, b in color_list
            ]
            def style_application(col):
                return color_styles if col.name == "Appliance" else [""] * len(col)
                
            st.dataframe(legend_df.style.apply(style_application, axis=0), use_container_width=True, height=260)
            
            # Export section
        st.markdown("### 📤 Export Your Report")
        export_df = usage_df[["Appliance", "Quantity", "Hours_per_day", "Power (Watts)", "Monthly_kWh"]]
        towrite = BytesIO()
        export_df.to_csv(towrite, index=False)
        towrite.seek(0)
        st.download_button("📥 Download Usage Report (CSV)", towrite, file_name="energy_report.csv", mime="text/csv")

else:
    st.info("Please select at least one appliance to get started.")
