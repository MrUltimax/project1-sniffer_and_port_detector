<h1>Signature-based NIDS/IPS </h1>
A lightweight Network Intrusion Detection System (NIDS) alongwith Intrusion Prevention System built using Python and Scapy.
This project monitors real-time network traffic and detects port scanning attacks based on behavioral analysis.
It also blocks temporarily block the Attacking IP address.

<h3>Overview</h3>

This project is designed as a learning and research-oriented NIDS/IPS prototype, focusing on:

- Real-time packet sniffing
- Detection of suspicious network behavior
- Blocking the suspicious IP Addresses
- Lightweight design suitable for IoT environments

Packet sniffing tools are commonly used in network monitoring to capture and analyze traffic flowing across a network

<h3>Features:</h3>
<ul>
<li>Live packet sniffing</li>
<li>TCP/UDP traffic monitoring</li>
<li>Port scan detection (threshold-based)</li>
<li>Slow scan detection (time-window based)</li>
<li>Desktop notifications for alerts</li>
<li>Logging of detected attacks</li>
<li>Behavior-based detection approach</li>
</ul>


<h3>Technologies Used</h3>
<ul>
<li>Python 3</li>
<li>Scapy – packet manipulation and sniffing</li>
<li>Linux networking tools (for packet capture)</li>
</ul>

<h3>Installation</h3>

<h4>Clone the repository:</h4>
git clone https://github.com/MrUltimax/project1-sniffer_and_port_detector

cd project1-sniffer_and_port_detector

<h4>Install dependencies:</h4>
pip install -r requirements.txt

<h3>Usage</h3>
<h4>Run the detector (requires root privileges):</h4>
sudo python3 scan_detector.py

      ⚠️Root access is required because packet sniffing needs permission to capture raw network traffic.

<h3>The system monitors incoming packets and:</h3>
<ol>
<li>Extracts source IP and destination port</li>
<li>Tracks unique ports accessed by each IP</li>
<li>Applies:</li><ul>
     <li>Threshold detection (number of ports scanned)</li>
     <li>Time-window analysis (slow scan detection)</li>
</ul>
<li>Generates alerts if suspicious behavior is detected</li>
</ol>

<h3>Author</h3>
MrUltimax

<h3>Contribute</h3>
Feel free to fork, improve, and submit pull requests!

<h3>License</h3>
This project is open-source and available under the MIT License.

<h3>Note</h3>
This is my first Project and may still contain errors or bugs

<h4>Preview:</h4>
<img width="1053" height="762" alt="image" src="https://github.com/user-attachments/assets/07c8cb05-857f-456c-857d-6d9d654dbb7e" />

