#!/usr/bin/python3

startVpn = 2000
quantity = 500
with open('addresslist.csv', 'w') as file:
    for vpn in range(startVpn, startVpn+quantity):
        file.write(f'10.{int((vpn + 10) / 256)}.{(vpn + 10) % 256}.1\n')