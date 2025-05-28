from crewai.tools import tool
import psutil
import subprocess
import platform
import time
from datetime import datetime
import os 

@tool("advanced_network_metrics_tool")
def advanced_network_metrics_tool() -> str:
    """
    Collects extended system and network metrics including CPU, Memory,
    Disk, Network traffic, Latency, and Jitter.
    """

    report = []

    cpu = psutil.cpu_percent(interval=1)
    report.append(f"CPU Usage: {cpu}%")
    if cpu > 85:
        report.append("❗ High CPU Usage Alert!")

    mem = psutil.virtual_memory()
    mem_available_gb = mem.available / (1024 ** 3)
    report.append(f"Memory Available: {round(mem_available_gb, 2)} GB ({mem.percent}% used)")
    if mem_available_gb < 2:
        report.append("❗ Low Available Memory Alert!")

    disk = psutil.disk_usage('/')
    report.append(f"Disk Usage: {disk.percent}%")
    if disk.percent > 85:
        report.append("❗ High Disk Usage Alert!")

    net = psutil.net_io_counters()
    net_sent = round(net.bytes_sent / (1024 ** 2), 2)
    net_recv = round(net.bytes_recv / (1024 ** 2), 2)
    report.append(f"Network Sent: {net_sent} MB, Received: {net_recv} MB")
    if net_sent > 10000:
        report.append("❗ High Network Sent Alert!")
    if net_recv > 10000:
        report.append("❗ High Network Receive Alert!")

    net_interfaces = psutil.net_if_stats()
    for iface, stat in net_interfaces.items():
        report.append(f"Interface '{iface}': isup={stat.isup}, speed={stat.speed}Mbps, duplex={stat.duplex}")

    targets = ["8.8.8.8", "1.1.1.1", "google.com", "trigent.com"]
    latencies = []

    for host in targets:
        try:
            cmd = ["ping", "-n", "3", host] if platform.system() == "Windows" else ["ping", "-c", "3", host]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout

            times = []
            for line in output.split("\n"):
                if "time=" in line.lower():
                    try:
                        time_part = line.lower().split("time=")[1].split()[0].replace("ms", "").strip()
                        times.append(float(time_part))
                    except Exception as parse_err:
                        report.append(f"❗ Error parsing latency value for {host}: {str(parse_err)}")

            if times:
                avg_latency = sum(times) / len(times)
                jitter = max(times) - min(times) if len(times) > 1 else 0
                latencies.append(avg_latency)

                report.append(f"Ping to {host}: Avg Latency={round(avg_latency, 2)}ms, Jitter={round(jitter, 2)}ms")
                if avg_latency > 100:
                    report.append(f"❗ High Latency to {host}")
                if jitter > 20:
                    report.append(f"❗ High Jitter to {host}")
            else:
                report.append(f"❗ Ping to {host} failed or no latency data found")
        except Exception as e:
            report.append(f"❗ Ping error for {host}: {str(e)}")


    os.makedirs("logs", exist_ok=True)

    log_filename = f"logs/metrics_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write("\n".join(report))

    return "\n".join(report)

