from scapy import sniff

def callback(packet):
	if packet.haslayer("IP");
		src = packet["IP"].src
		dest = packet["IP"].dst
		protocol = packet["IP"].proto
		
		print (f"Source = {src} -> Destintion = {dest} | protocol = {protocol}")

sniff(prn=callback, count=10)
