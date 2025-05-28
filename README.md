# 🛰️ Network Monitoring System

An intelligent, agent-based system using [CrewAI](https://github.com/joaomdmoura/crewAI) for real-time system and network performance monitoring, anomaly detection, and automated reporting with system alerts.

---

## 🚀 Features

- 📡 **Real-time Monitoring**: Collects CPU, memory, disk usage, network I/O, and latency.
- 🔍 **Anomaly Detection**: Identifies issues, classifies severity, and finds potential root causes.
- 📑 **Automated Reporting**: Generates detailed Markdown reports and sends system alerts.
- 🤖 **CrewAI Agents**: Modular multi-agent architecture for clarity and collaboration.

---

## 🛠️ Tech Stack

- **Python**
- **CrewAI** – for multi-agent orchestration
- **Langchain / OpenAI / LLM** – for natural language understanding (via `llm_config.py`)
- **Custom Tools** – for system monitoring and alerts (`tools/` directory)

---

## 🧠 Agents Overview

1. **Network Monitoring Agent**
   - Gathers live system and network performance metrics.
   - Detects violations and generates a summary.

2. **Anomaly Detection Agent**
   - Analyzes the monitoring summary.
   - Classifies severity and identifies root causes.

3. **Reporting Agent**
   - Creates a Markdown report and triggers system alerts.

---

## 📂 Project Structure

Network-Monitoring-System/
├── tools/
│ ├── advanced_network_metrics_tool.py
│ └── system_alert_tool.py
├── llm_config.py
├── main.py (or your main script file)
└── README.md

---

## 📦 Setup Instructions

1. **Clone the repository**
   
   git clone https://github.com/maheshvg24/Network-Monitoring-System.git
   cd Network-Monitoring-System

3. **Create a virtual environment**
   
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

5. **Install dependencies**
   
pip install -r requirements.txt

7. **Configure environment variables**
   
Create a .env file and add:
OPENAI_API_KEY=your_openai_key_here

9. **Run the system**
    
python main.py
