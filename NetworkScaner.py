#! /usr/bin/env python
from scapy.all import *

networkName = "192.168.1.0/24"

def Arp():
    alive, dead = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=networkName),timeout = 10)

    dic = {}
    for i in range(0,len(alive)):
        dic[alive[i][1].psrc] = alive[i][1].hwsrc
    return dic
    



hwDic = Arp()

for ip, hw in hwDic.items():
    print ip, hw 
