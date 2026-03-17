# project1-sniffer_and_port_detector
After working on my project, i have updated my NIDS and added some new feature,
1. After starting "scan_detector.py" on any type of scan, an alert will be sent to your device
2. I have added feature of notification to it.
3. This code now tells about the port, destination and source of scan.
4. This code now create an access log and a blacklist on sniffing a scan.

My main project is "scan_detecter.py". so,"sniffer.py" is same as last time

This code only use scapy for port sniffing, for version, you can check requirement.txt

Since this code use scapy, root permission is required for running it, use the command as:

sudo python scan_detector.py

<img width="600" height="189" alt="image" src="https://github.com/user-attachments/assets/97441496-e8b3-44b1-aa58-1f21ea0e5e08" />
                                            img:Sniffer.py

<img width="1053" height="762" alt="image" src="https://github.com/user-attachments/assets/07c8cb05-857f-456c-857d-6d9d654dbb7e" />
                                          img:scan_detector.py
