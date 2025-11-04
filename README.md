☀️ AI Energy Advisor – Intelligent Power Optimization for Nigerian Households

The AI Energy Advisor is an intelligent web application designed to help users understand and optimize their electricity consumption. It estimates energy usage, calculates monthly costs, and provides actionable recommendations — helping households make smarter, cost-effective, and sustainable energy decisions.

Now enhanced with a smarter AI logic engine, multi-appliance selection, and integration support for SolarPeer360, this version moves closer to real-time, AI-driven energy advisory for the future of decentralized solar systems.

🚀 Features

🔢 Multi-Appliance Selection: Choose multiple devices, quantities, and usage hours at once.

⚡ Smart Energy Estimation: Calculates total energy usage (kWh) and monthly cost.

🌍 Dynamic Energy Source Comparison: Compare NEPA, generator, and solar costs in real time.

🧠 AI-Powered Insights: Recommends ways to reduce consumption, shift load time, or transition to solar.

🔋 Adaptive Suggestions: Identifies energy waste and provides personalized reduction strategies.

☀️ SolarPeer360 Integration-Ready: Designed to interface with the P2P solar sharing platform for future expansion.

🧰 Tech Stack

Python 3.9+ – Core logic and computations

Streamlit – User interface and visualization

Pandas & NumPy – Data analysis and processing

Scikit-learn (optional) – For predictive model integration

Matplotlib / Seaborn (optional) – Visual analytics

📁 Folder Structure
📂 Energy Advisor/
├── appliance_power_ratings.csv     # Appliance power data (Watts)
├── energy_advisor_app.py           # Main Streamlit app
├── requirements.txt                # Dependencies
├── README.md                       # Project overview
└── assets/                         # (optional) Screenshots or visuals

⚙️ Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/ayatullah-hanif/ai-energy-advisor.git
cd ai-energy-advisor

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
streamlit run energy_advisor_app.py


The app launches locally at: http://localhost:8501

📊 Data Source

Power ratings derived from Nigerian household averages and national appliance consumption data.

Tariff and fuel rate estimates obtained from NERC, DPR, and verified market statistics (2024).

🧠 AI Recommendation Logic

The upgraded AI module applies a hybrid rule-based and predictive approach to energy optimization:

Analyzes selected appliances and daily usage patterns.

Predicts high-cost energy behavior based on tariff and load type.

Recommends optimal adjustments in usage time or quantity.

Advises when solar power becomes the cheaper or more efficient alternative.

🔮 Future Enhancements

🌐 Integration with Edge AI for real-time data processing via local IoT sensors.

📡 Connection to SolarPeer360 P2P network for solar cost comparison and sharing suggestions.

📱 Mobile-friendly version with offline support for rural users.

📊 Energy analytics dashboard for visual consumption monitoring.

🤝 Contributing

Pull requests are welcome! Whether improving the AI logic, enhancing UI, or adding predictive analytics — contributions are encouraged to help expand access to smarter, cleaner energy use.

📜 License

This project is released under the MIT License — free for modification and open-source collaboration.
