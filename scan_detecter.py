from scapy.all import sniff
from collections import defaultdict

scan_tracker = defaultdict(set)
alerted = set()

def packet_callback(packet):
	if packet.haslayer("IP") and packet.haslayer("TCP"):
		src = packet["IP"].src
		dest = packet["TCP"].dport
		
		scan_tracker[src].add(dest)
		
		if len(scan_tracker[src]) > 10 and src not in alerted:
		    print(f"ALERT! port scanning from {src} ")
		    alerted.add(src)

sniff(prn=packet_callback, store=0)
	
	
