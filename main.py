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

from vmanage_api import rest_api_lib
from includes import *
from vmanage_credentials import *
import json


def create_feature_template(variables, payload):

    for variable in variables:
        payload = payload.replace(f'~~~{variable}~~~', f'{variables[variable]}')
    url = '/template/feature'
    response = vmanage.post_request(url, json.loads(payload))
    return response['templateId']


if __name__ == '__main__':
    vmanage = rest_api_lib(vmanage_ip, vmanage_user, vmanage_password)

    service_vpns = ''
    for vpn in range(150, 200):

        # Create VPN

        elements = {
            'templateName': f'FIS_VPN_{vpn}',
            'templateDescription': f'FIS VPN {vpn}',
            'vpn-id': f'{vpn}',
            'vpn_name': f'VPN {vpn}'
        }
        vpn_template_id = create_feature_template(elements, vpn_template)

        # Create Subinterface

        subnet = f'10.{int((vpn + 10) / 256)}.{(vpn + 10) % 256}.1/24'
        elements = {
            'templateName': f'FIS_SUBINTERFACE_{vpn}',
            'templateDescription': f'FIS SUBINTERFACE {vpn}',
            'vpn_if_name': f'GigabitEthernet3.{vpn}',
            'vpn_if_description': f'VPN {vpn}',
            'if_ip_address': subnet
        }
        subinterface_template_id = create_feature_template(elements, subinterface_template)

        # Add VPN and Subinterface to "service_vpns" variable for device template

        service_vpn = {
          "templateId": vpn_template_id,
          "templateType": "cisco_vpn",
          "subTemplates": [
            {
              "templateId": subinterface_template_id,
              "templateType": "cisco_vpn_interface"
            }
          ]
        }
        print(f'{vpn}: {service_vpn}')
        service_vpns += json.dumps(service_vpn, indent=2) + ','

    # Create Device Template

    elements = {
        'templateName': f'FIS_DC_EDGE_1',
        'templateDescription': f'FIS DC Edge for VPNs 150-199',
        'service_vpns': service_vpns
    }
    for element in elements:
        device_template = device_template.replace(f'~~~{element}~~~', f'{elements[element]}')
    url = '/template/device/feature'
    response = vmanage.post_request(url, json.loads(device_template))
    print(f"Device Template: {response['templateId']}")

    vmanage.logout()

# [END gae_python38_app]
