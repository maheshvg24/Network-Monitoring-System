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


