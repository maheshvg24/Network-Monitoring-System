from crew import crew
import time
from datetime import datetime

INTERVAL = 60  

while True:
    print(f"\n🕒 Starting system monitoring at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    result = crew.kickoff()

    print("=== MONITORING RESULT ===")
    print(result)

    print(f"✅ Next check in {INTERVAL} seconds...\n")
    time.sleep(INTERVAL)
