from scapy.all import sniff
from collections import defaultdict
import os
import time
import platform
import subprocess
import signal
import sys
from plyer import notification  # Ensure you have installed plyer

# Configuration
PORT_SCAN_THRESHOLD = 10
TIME_WINDOW = 30
ALERT_COOLDOWN = 60

# Tracking
scan_tracker = defaultdict(set)
scan_time = {}
alert_time = {}
blocked_ips = []  # To track for graceful unblocking

def block_ip(ip):
    """Detects OS and applies firewall rule to block the IP."""
    current_os = platform.system()
    try:
        if ip not in blocked_ips:
            if current_os == "Linux":
                subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            elif current_os == "Windows":
                rule_name = f"NIDS_Block_{ip.replace('.', '_')}"
                subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                                f"name={rule_name}", "dir=in", "action=block", f"remoteip={ip}"], check=True)
            
            blocked_ips.append(ip)
            print(f"[IPS] Blocked attacker: {ip}")
    except Exception as e:
        print(f"[ERROR] Could not block {ip}: {e}")

def unblock_all():
    """Removes all rules created during this session."""
    print("\n[SYSTEM] Cleaning up firewall rules...")
    current_os = platform.system()
    for ip in blocked_ips:
        try:
            if current_os == "Linux":
                subprocess.run(["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"], check=True)
            elif current_os == "Windows":
                rule_name = f"NIDS_Block_{ip.replace('.', '_')}"
                subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule", f"name={rule_name}"], check=True)
            print(f"[CLEANUP] Unblocked: {ip}")
        except Exception as e:
            print(f"[ERROR] Failed to unblock {ip}: {e}")

def send_notification(ip):
    """Sends a cross-platform desktop notification."""
    try:
        notification.notify(
            title="NIDS ALERT",
            message=f"Port scan detected from {ip}. Attacker has been blocked.",
            timeout=10
        )
    except Exception:
        pass # Fallback if notification system fails

def log_alert(ip):
    """Logs the alert to a local file."""
    with open("alerts.log", "a") as f:
        f.write(f"{time.ctime()} - BLOCKED: {ip}\n")

def signal_handler(sig, frame):
    """Triggers when Ctrl+C is pressed."""
    unblock_all()
    print("[SYSTEM] NIDS stopped safely.")
    sys.exit(0)

# Register the Ctrl+C handler
signal.signal(signal.SIGINT, signal_handler)

def packet_callback(packet):
    if packet.haslayer("IP") and packet.haslayer("TCP"):
        src = packet["IP"].src
        dst_port = packet["TCP"].dport
        flags = packet["TCP"].flags

        # Only track SYN packets (typical of a port scan)
        if flags == "S":
            current_time = time.time()
            
            if src not in scan_time:
                scan_time[src] = current_time

            # Reset window if time exceeded
            if current_time - scan_time[src] > TIME_WINDOW:
                scan_tracker[src].clear()
                scan_time[src] = current_time

            scan_tracker[src].add(dst_port)

            # Threshold check
            if len(scan_tracker[src]) > PORT_SCAN_THRESHOLD:
                if src not in alert_time or current_time - alert_time[src] > ALERT_COOLDOWN:
                    print(f"\n[!!!] ALERT: Port scan detected from {src}!")
                    
                    block_ip(src)
                    send_notification(src)
                    log_alert(src)
                    
                    alert_time[src] = current_time

print("NIDS/IPS Active. Monitoring for SYN scans...")
print("Press Ctrl+C to stop and clear firewall rules.")
sniff(prn=packet_callback, store=0)
