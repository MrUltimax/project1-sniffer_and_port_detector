
PORT_SCAN_THRESHOLD = 10
TIME_WINDOW = 30
ALERT_COOLDOWN = 60

proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

def send_notification(ip):
    os.system(f'notify-send "NIDS ALERT" "Port scan detected from {ip}"')

def log_alert(ip):
    with open("alerts.log", "a") as f:
        f.write(f"{time.ctime()} - Port scan detected from {ip}\n")

    with open("blacklist.txt", "a") as f:
        f.write(ip + "\n")

def packet_callback(packet):

    if packet.haslayer("IP"):

        src = packet["IP"].src
        dst = packet["IP"].dst
        proto_num = packet["IP"].proto
        proto = proto_map.get(proto_num, "OTHER")

        dst_port = None

        if packet.haslayer("TCP"):
            dst_port = packet["TCP"].dport
        elif packet.haslayer("UDP"):
            dst_port = packet["UDP"].dport

        print(f"[TRAFFIC] {src} -> {dst} | {proto} | Port {dst_port}")

        if packet.haslayer("TCP"):

            current_time = time.time()

            # initialize scan timer
            if src not in scan_time:
                scan_time[src] = current_time

            # reset window if time exceeded
            if current_time - scan_time[src] > TIME_WINDOW:
                scan_tracker[src].clear()
                scan_time[src] = current_time

            scan_tracker[src].add(dst_port)

            if len(scan_tracker[src]) > PORT_SCAN_THRESHOLD:

                if src not in alert_time or current_time - alert_time[src] > ALERT_COOLDOWN:

                    print(f"[ALERT] Possible port scan detected from {src}")

                    send_notification(src)
                    log_alert(src)

                    alert_time[src] = current_time

sniff(prn=packet_callback, store=0)
