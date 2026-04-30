<h1>Lightweight NIDS/IPS for Port Scan Detection</h1>

<p>
A lightweight <b>Network Intrusion Detection and Prevention System (NIDS/IPS)</b> implemented in Python using Scapy.
This system monitors real-time network traffic, detects suspicious scanning behavior, and automatically blocks malicious IP addresses.
</p>

<hr>

<h2>Overview</h2>
<p>
This project is designed as a learning and research-oriented prototype focusing on real-time network monitoring and lightweight security mechanisms,
particularly for environments with limited resources such as IoT devices.
</p>

<ul>
  <li>Real-time packet sniffing</li>
  <li>Detection of suspicious network behavior</li>
  <li>Automatic blocking of malicious IPs</li>
  <li>Lightweight design</li>
</ul>

<hr>

<h2>How It Works</h2>
<ol>
  <li>Captures packets using Scapy</li>
  <li>Extracts source IP and destination ports</li>
  <li>Tracks unique ports accessed per IP</li>
  <li>Applies detection logic:
    <ul>
      <li>Threshold-based detection (fast scans)</li>
      <li>Time-window analysis (slow scans)</li>
    </ul>
  </li>
  <li>Triggers alerts and blocks attacker IP</li>
</ol>

<hr>

<h2>Features</h2>
<ul>
  <li>Live packet sniffing</li>
  <li>TCP/UDP traffic monitoring</li>
  <li>Port scan detection (threshold-based)</li>
  <li>Slow scan detection (time-window based)</li>
  <li>Desktop notifications</li>
  <li>Attack logging</li>
  <li>Behavior-based detection approach</li>
</ul>

<hr>

<h2>Technologies Used</h2>
<ul>
  <li>Python 3</li>
  <li>Scapy</li>
  <li>Plyer</li>
  <li>Linux Firewall (iptables) / Windows Firewall</li>
</ul>

<hr>

<h2>Installation</h2>
<pre>
git clone https://github.com/MrUltimax/project1-sniffer_and_port_detector
cd project1-sniffer_and_port_detector
pip install -r requirements.txt
</pre>

<hr>

<h2>Usage</h2>
<pre>
sudo python3 scan_detector.py
</pre>

<p><b>Note:</b> Root privileges are required to capture network packets.</p>

<hr>

<h2>Detection Logic</h2>
<ul>
  <li>Tracks number of unique ports accessed by an IP</li>
  <li>Analyzes behavior within a time window</li>
  <li>Triggers alerts when thresholds are exceeded</li>
</ul>

<hr>

<h2>Limitations</h2>
<ul>
  <li>Focused mainly on TCP SYN scans</li>
  <li>May produce false positives</li>
  <li>Does not handle advanced evasion techniques</li>
</ul>

<hr>

<h2>Future Work</h2>
<ul>
  <li>Support for UDP and stealth scan detection</li>
  <li>Machine learning-based anomaly detection</li>
  <li>Integration with live traffic analyzer dashboard</li>
  <li>Optimization for IoT environments</li>
</ul>

<hr>

<h2>Author</h2>
<p>MrUltimax</p>

<hr>

<h2>Contributing</h2>
<p>Feel free to fork, improve, and submit pull requests.</p>

<hr>

<h2>License</h2>
<p>MIT License</p>

<hr>

<h2>📝 Note</h2>
<p>This is an early-stage project developed for learning and research purposes and may contain bugs.</p>
