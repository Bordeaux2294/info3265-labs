import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    print(packet)
   

if __name__ = "__main__":
    sniff("eth0")
