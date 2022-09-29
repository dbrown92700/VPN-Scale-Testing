#!/usr/bin/python3
"""
Copyright (c) 2012 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
__author__ = "David Brown <davibrow@cisco.com>"
__contributors__ = []
__copyright__ = "Copyright (c) 2012 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
from cliIncludes import *
from vmanage_credentials import *
from vmanage_api import rest_api_lib

vrf_definitions = ''
vrf_name_servers = ''
subinterfaces = ''

for vpn in range(vpnStart, vpnEnd+1):
    vrf_definitions += f'''vrf definition {vpn}
 description VPN {vpn}
 rd          1:{vpn}
 address-family ipv4
  route-target export 1:{vpn}
  route-target import 1:{vpn}
  exit-address-family
 !
 address-family ipv6
  exit-address-family
 !
!
'''
    vrf_name_servers += f'''ip name-server vrf {vpn} 1.1.1.1 8.8.8.8
'''
    subinterfaces += f'''interface GigabitEthernet3.{vpn}
 description VPN {vpn}
 no shutdown
 arp timeout 1200
 encapsulation dot1Q {vpn}
 vrf forwarding {vpn}
 ip address {{{{VPN {vpn} Interface Address}}}} 255.255.255.0
 no ip redirects
 ip mtu    1496
exit
'''

cliTemplate = cliTemplate\
    .replace('~~~vrf-definitions~~~', vrf_definitions.rstrip('\n'))\
    .replace('~~~vrf-name-servers~~~', vrf_name_servers.rstrip('\n'))\
    .replace('~~~subinterfaces~~~', subinterfaces.rstrip('\n'))

with open(f'output/FIS_VPN{vpnStart}-{vpnEnd}.cfg', "w") as file:
    file.write(cliTemplate)

vmanage = rest_api_lib(vmanage_ip, vmanage_user, vmanage_password)
vmanage_template = {
   "templateName": f'FIS_VPN{vpnStart}-{vpnEnd}',
   "templateDescription": f'[AutoCLI] FIS VPNs {vpnStart}-{vpnEnd}',
   "deviceType": deviceType,
    "factoryDefault": False,
    "configType": "file",
    "templateConfiguration": cliTemplate
}

templateId = vmanage.post_request('/template/device/cli', vmanage_template)
vmanage.logout()

print(f'templateId: {templateId}')

with open(f'output/addresslist{vpnStart}-{vpnEnd}.csv', 'w') as file:
    for vpn in range(vpnStart, vpnEnd+1):
        file.write(f'10.{int((vpn + 10) / 256)}.{(vpn + 10) % 256}.1,')
