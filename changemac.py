#!/usr/bin/python
import os
import time
from scapy.all import *
iplist=[]
gateway='192.168.8.30'
octet=raw_input("Enter the three octet of the ip\n")
for ap in range(0,253):
   iplist.append(octet+'.'+'%s' % ap)
iplist.remove(octet+'.1')
iplist.remove(octet+'.30')
def change():
  for man in range(0,250):
     os.system('ifconfig wlan0 down')
     os.system('macchanger -r wlan0')
     os.system('ifconfig wlan0 %s' % iplist[man])
     os.system('ifconfig wlan0 up')
    
     ip=IP()
     ip.src=iplist[man]
     ip.dst='192.168.8.30'
     icmp=ICMP()
     icmp.type=8
     icmp.code=0
     send(ip/icmp)

change()
