<h1>Lightweight Packet Sniffer & Port Scan Detector </h1>
A lightweight Network Intrusion Detection System (NIDS) built using Python and Scapy.
This project monitors real-time network traffic and detects port scanning attacks based on behavioral analysis.

<h3>Overview</h3>

This project is designed as a learning and research-oriented NIDS prototype, focusing on:

- Real-time packet sniffing
- Detection of suspicious network behavior
- Lightweight design suitable for IoT environments

Packet sniffing tools are commonly used in network monitoring to capture and analyze traffic flowing across a network

<h3>Features:</h3>
- Live packet sniffing
- TCP/UDP traffic monitoring
- Port scan detection (threshold-based)
- Slow scan detection (time-window based)
- Desktop notifications for alerts
- Logging of detected attacks
- Behavior-based detection approach

Installation
pip install -r requirements.txt

Run
sudo python3 detector.py

<img width="600" height="189" alt="image" src="https://github.com/user-attachments/assets/97441496-e8b3-44b1-aa58-1f21ea0e5e08" />
                                            img:Sniffer.py


<img width="1053" height="762" alt="image" src="https://github.com/user-attachments/assets/07c8cb05-857f-456c-857d-6d9d654dbb7e" />
                                          img:scan_detector.py
