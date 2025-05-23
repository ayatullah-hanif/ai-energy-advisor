# 🔌 AI Energy Saving Advisor

A simple and intelligent web app that helps users estimate their energy usage, calculate monthly electricity costs, and receive smart recommendations to reduce power consumption. Built with Streamlit and powered by local appliance usage data in Nigeria.

---

## 🚀 Features
- Select appliance, usage hours, and quantity
- Choose energy source: NEPA, Generator, or Solar
- Calculates estimated monthly energy consumption (in kWh)
- Predicts electricity costs based on current tariffs
- Offers AI-powered energy-saving tips

---

## 🧰 Tech Stack
- Python 🐍
- Streamlit 🧼
- Pandas 📊

---

## 📁 Folder Structure
```bash
📂 Energy Project/
├── appliance_power_ratings.csv     # Appliance types and average power usage (Watts)
├── energy_advisor_app.py          # Main Streamlit app
├── README.md                      # Project overview
└── requirements.txt               # Dependencies
```

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-energy-advisor.git
cd ai-energy-advisor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run energy_advisor_app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📊 Data Source
- Power ratings are based on averages from Nigerian appliance benchmarks.
- Tariff estimates sourced from NERC and local market rates as of 2024.

---

## 🧠 AI Recommendation Logic
Basic rule-based AI suggests tips like:
- Reduce usage time
- Switch to inverter/solar alternatives
- Identify high-cost appliances

---

## 📬 Author
Ayatullah Hanif
https://github.com/ayatullah-hanif
Built for the May 2025 3MTT Knowledge Showcase.

---

## 📌 License
This project is licensed under the MIT License.
