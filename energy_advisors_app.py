# energy_advisor_app.py (Streamlit version)

import pandas as pd
import streamlit as st

# Load appliance data from CSV
def load_appliance_data(csv_path):
    return pd.read_csv(csv_path)

# Calculate energy usage and cost
def calculate_energy_cost(power_watts, quantity, hours_per_day, days_per_month, source='NEPA'):
    tariff = {
        'NEPA': 74,            # ₦ per kWh (Band B avg)
        'Generator': 170,      # ₦ per kWh (petrol-based est.)
        'Solar': 20            # ₦ per kWh (maintenance est.)
    }
    energy_kwh = (power_watts * quantity * hours_per_day * days_per_month) / 1000
    cost = energy_kwh * tariff.get(source, 74)
    return round(energy_kwh, 2), round(cost, 2)

# Generate advice based on energy use
def get_advice(energy_kwh, cost):
    tips = []
    if energy_kwh > 100:
        tips.append("Consider reducing usage hours or quantity.")
    if cost > 5000:
        tips.append("You may want to switch to inverter-based or solar appliances.")
    if not tips:
        tips.append("Your setup is energy-efficient. Keep it up!")
    return tips

# Streamlit UI
def main():
    st.title("🔌 AI Energy Saving Advisor")
    st.write("Estimate your energy usage and get smart recommendations.")

    # Use your actual CSV file path here
    csv_path = "appliance_power_ratings.csv"
    df = load_appliance_data(csv_path)

    # Inputs
    appliance = st.selectbox("Select an appliance:", df['Appliance'].unique())
    quantity = st.number_input("How many do you use?", min_value=1, value=1)
    hours_per_day = st.number_input("Usage hours per day:", min_value=1.0, max_value=24.0, value=6.0)
    days_per_month = st.slider("How many days per month do you use it?", 1, 31, 30)
    source = st.selectbox("Select energy source:", ['NEPA', 'Generator', 'Solar'])

    if st.button("Calculate Consumption"):
        power_watts = df[df['Appliance'] == appliance]['Power (Watts)'].values[0]
        energy_kwh, cost = calculate_energy_cost(power_watts, quantity, hours_per_day, days_per_month, source)

        st.success(f"Estimated Monthly Energy Use: {energy_kwh} kWh")
        st.success(f"Estimated Monthly Cost: ₦{cost}")

        st.subheader("💡 Recommendations")
        for tip in get_advice(energy_kwh, cost):
            st.write(f"- {tip}")

if __name__ == '__main__':
    main()
