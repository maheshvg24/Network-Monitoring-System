from crewai import Agent, Task, Crew, Process
from tools.advanced_network_metrics_tool import advanced_network_metrics_tool
from llm_config import llm
from tools.system_alert_tool import system_notification_alert_tool
from datetime import datetime

network_monitoring_agent = Agent(
    role="Network Monitoring Agent",
    goal="Collect system and network performance metrics and identify potential issues.",
    backstory="A vigilant agent responsible for monitoring live system health using advanced tools. You detect abnormalities and raise flags when something is off.",
    tools=[advanced_network_metrics_tool],
    llm=llm,
    memory=True,
    verbose=True
)

anomaly_detection_agent = Agent(
    role="Anomaly Detection Agent",
    goal="Analyze monitoring reports and determine severity and root cause of any anomalies.",
    backstory="A data-driven analytical agent who specializes in understanding anomalies, assessing their impact, and classifying their severity to guide proper response.",
    llm=llm,
    memory=True,
    verbose=True
)


reporting_agent = Agent(
    role="Reporting Agent",
    goal="Generate report and notify user through system alerts.",
    backstory="You finalize the analysis and send visual+audible alerts if required.",
    tools=[system_notification_alert_tool],
    llm=llm,
    memory=True,
    verbose=True,
    allow_delegation=False
)


monitor_task = Task(
    description="""
    Collect real-time system and network performance metrics including:
    - CPU, memory, disk usage
    - Network I/O
    - Interface status
    - Latency and jitter via ping
    Use the advanced_network_metrics_tool to generate a performance summary and highlight any threshold violations or alerts.
    """,
    expected_output="""
    A summarized system health report in natural language. Include alerts if any metric exceeds thresholds.
    Example:
    - CPU Usage: 92% ❗ High
    - Memory Available: 1.8 GB ❗ Low
    - Latency to 8.8.8.8: 122ms ❗ High
    """,
    tools=[advanced_network_metrics_tool],
    agent=network_monitoring_agent
)

anomaly_task = Task(
    description="""
    Read the output from the monitoring report and analyze each alert in detail.
    - Classify the anomaly (e.g., CPU Overload, Memory Starvation)
    - Assign severity: Low, Medium, High
    - Suggest potential root cause for each alert.
    """,
    expected_output="""
    Detailed analysis report listing:
    - Type of Anomaly
    - Severity Level
    - Possible Root Cause
    """,
    agent=anomaly_detection_agent
)

output_filename = f"network_alert_report_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"


report_task = Task(
    description="""
    Using the analysis from anomaly detection, generate a well-formatted Markdown report.
    Include:
    - Executive Summary
    - Metric Snapshot
    - Anomaly Details
    - Suggested Actions
    If no anomalies are found, state clearly: "✅ System healthy. No report generated."
    """,
    expected_output="Final report saved as markdown file.",
    agent=reporting_agent,
    output_file = output_filename
)

crew = Crew(
    agents=[network_monitoring_agent, anomaly_detection_agent, reporting_agent],
    tasks=[monitor_task, anomaly_task, report_task],
    process=Process.sequential
)
