#!/bin/sh
sudo sudo modprobe slip
sudo slattach -p slip -s 9600 /dev/ttyS0 &
sudo ifconfig sl0 192.168.100.101 netmask 255.255.255.0 broadcast 255.255.255.255 mtu 200


