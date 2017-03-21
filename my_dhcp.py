
# Command to listen to DHCP packet and store in variable
# dhcp_packet = sniff(filter="port 68 and port 67" , iface="en0")


import subprocess
import logging
import random
import sys


try:
from scapy.all import *

except ImportError:
    print("Scapy package for Python is not installed on your system.")

print("Make sure to run this program as ROOT !")


subprocess.call(["ifconfig", "eth0", "promisc"])


conf.checkIPaddr = False


def gen_DHCP_seq():

    x_id = random.randrange(1, 1000000)
	hw = str(RandMAC())
	hw_str = mac2str(hw)


    dhcp_dis_pkt = Ether(dst="ff:ff:ff:ff:ff:ff", src=hw)/IP(src="0.0.0.0",dst="255.255.255.255") / UDP(sport=68,dport=67)/BOOTP(op=1, xid=x_id, chaddr=hw_str)/DHCP(options=[("message-type","discover"),("end")])

    answd, unanswd = srp(dhcp_dis_pkt, iface="eth0", timeout = 2.5, verbose=0)












