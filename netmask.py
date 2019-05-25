#!/usr/bin/python3.6

import sys

if int(sys.argv[1]) > 32:
    sys.exit('Out of range')
bits = int(sys.argv[1])
addresses = 2**(32 - bits)
usable = addresses - 2

i = 0
octets = [''] * 4
fullOctet = bits // 8
bits %= 8

while bits > 0:
    octets[fullOctet] = octets[fullOctet] + '1'
    bits -= 1
octets[fullOctet] = octets[fullOctet].ljust(8,'0')

while fullOctet >= 0:
    octets[fullOctet] = octets[fullOctet].ljust(8,'1') 
    fullOctet -= 1

while i < 4:
    octets[i] = int(octets[i], 2)
    i += 1

netMask = '.'.join(str(e) for e in octets)
print("addresses: " + str(addresses) + " usable: " + str(usable) + " netmask: " + netMask)
