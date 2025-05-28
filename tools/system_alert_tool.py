from crewai.tools import tool
from plyer import notification
import platform

try:
    if platform.system() == "Windows":
        import winsound
except ImportError:
    winsound = None

@tool("system_notification_alert_tool")
def system_notification_alert_tool(alert_message: str) -> str:
    """
    Sends a desktop notification + plays a system alert sound when a critical alert is raised.
    Works on all platforms for popup notification.
    Plays a sound on Windows using winsound.
    """
    notification.notify(
        title="🚨 System Alert",
        message=alert_message,
        timeout=10
    )

    if platform.system() == "Windows" and winsound:
        try:
            winsound.Beep(1000, 1000)
        except Exception as e:
            return f"Popup sent, but sound failed: {str(e)}"

    return "✅ Desktop notification and alert sound triggered successfully"
