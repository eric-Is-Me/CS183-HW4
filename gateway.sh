#!/bin/bash

gateway=($(ip route | grep default))
netmask=($(ifconfig | grep netmask))
echo "${gateway[0]}: ${gateway[2]}"
echo "${netmask[2]}: ${netmask[3]}"
echo "device: ${gateway[4]}"
