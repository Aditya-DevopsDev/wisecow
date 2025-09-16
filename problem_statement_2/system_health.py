#!/usr/bin/env python3
import psutil
import logging

# Setup logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thresholds
CPU_THRESHOLD = 80  # %
MEM_THRESHOLD = 80  # %
DISK_THRESHOLD = 90  # %
PROC_THRESHOLD = 300  # number of processes

def check_system_health():
    alerts = []

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"⚠ High CPU usage: {cpu_usage}%")

    memory = psutil.virtual_memory()
    if memory.percent > MEM_THRESHOLD:
        alerts.append(f"⚠ High Memory usage: {memory.percent}%")

    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"⚠ Low Disk Space: {disk.percent}% used")

    processes = len(psutil.pids())
    if processes > PROC_THRESHOLD:
        alerts.append(f"⚠ Too many processes: {processes}")

    if alerts:
        for alert in alerts:
            logging.warning(alert)
            print(alert)
    else:
        msg = "✅ System health is normal"
        logging.info(msg)
        print(msg)

if __name__ == "__main__":
    check_system_health()
