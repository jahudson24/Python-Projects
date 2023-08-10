# Basic packet sniffer using Scapy
# Can be modified to filter different interfaces or protocols. Writes to PCAP file

from scapy.all import *

sniffer = sniff(prn=lambda x:x.summary(), filter="tcp", count=5)

print(sniffer)
wrpcap("sniffed-packets.pcap", sniffer)
