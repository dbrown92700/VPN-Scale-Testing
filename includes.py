#
# Device Template to be edited
#

template_id = "b93168f1-10cd-4c32-9af7-10bc3bb699bf"
device_template = """
{
  "templateName": "~~~templateName~~~",
  "templateDescription": "~~~templateDescription~~~",
  "deviceType": "vedge-C8000V",
  "deviceRole": "sdwan-edge",
  "configType": "template",
  "factoryDefault": false,
  "policyId": "",
  "featureTemplateUidRange": [],
  "draftMode": false,
  "connectionPreferenceRequired": true,
  "connectionPreference": true,
  "generalTemplates": [
    {
      "templateId": "53a550b2-208c-4cc5-8c47-d47eab17b8fa",
      "templateType": "cedge_aaa"
    },
    {
      "templateId": "fab62e1d-24fc-4660-a342-af3b22596afd",
      "templateType": "cisco_bfd"
    },
    {
      "templateId": "f0ca8d14-95dd-4400-9f7f-f21f482ebe89",
      "templateType": "cisco_omp"
    },
    {
      "templateId": "adacafdd-bd74-4cf4-ac12-ac2f853ff4bb",
      "templateType": "cisco_security"
    },
    {
      "templateId": "29b9e066-413b-43d0-b95d-ed008fb2e00b",
      "templateType": "cisco_system",
      "subTemplates": [
        {
          "templateId": "a9d6313f-1a3d-4afc-bf20-7d51d44eb9d3",
          "templateType": "cisco_logging"
        }
      ]
    },
    {
      "templateId": "3e6a9cb8-7690-44ef-a038-49acc9de2191",
      "templateType": "cisco_vpn",
      "subTemplates": [
        {
          "templateId": "8a197788-56d7-4768-9d27-5d7fc6a8cbac",
          "templateType": "cisco_vpn_interface"
        },
        {
          "templateId": "809405fc-5840-41f4-ba8a-13bfc4b9ad53",
          "templateType": "cisco_vpn_interface"
        }
      ]
    },
    {
      "templateId": "7990eef8-1a43-4cea-a1f5-f1ff6f8134e0",
      "templateType": "cisco_vpn",
      "subTemplates": [
        {
          "templateId": "0da883e8-f47d-4f36-ac6a-fbe2fe61341d",
          "templateType": "cisco_vpn_interface"
        }
      ]
    },
    ~~~service_vpns~~~
    {
      "templateId": "59ebcf8c-8f07-4871-8c5f-ec27654fb41a",
      "templateType": "cedge_global"
    },
    {
      "templateId": "81b54851-9d94-43dd-9c92-4cd611fe7cbd",
      "templateType": "cisco_banner"
    }
  ],
  "templateClass": "cedge"
}
"""


#
# The following are template definitions.
# Specific elements are variables with ~~~ delimiters.
#

vpn_template = """
{
  "templateName": "~~~templateName~~~",
  "templateDescription": "~~~templateDescription~~~",
  "templateType": "cisco_vpn",
  "deviceType": [
    "vedge-C8000V",
    "vedge-C8300-1N1S-4T2X",
    "vedge-C8300-1N1S-6T",
    "vedge-C8300-2N2S-6T",
    "vedge-C8300-2N2S-4T2X",
    "vedge-C8500-12X4QC",
    "vedge-C8500-12X",
    "vedge-C8500-20X6C",
    "vedge-C8500L-8S4X",
    "vedge-C8200-1N-4T",
    "vedge-C8200L-1N-4T"
  ],
  "factoryDefault": false,
  "templateMinVersion": "15.0.0",
  "configType": "xml",
  "resourceGroup": "global",
  "templateDefinition": {
    "vpn-id": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": ~~~vpn-id~~~
    },
    "name": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": "~~~vpn_name~~~",
      "vipVariableName": "vpn_name"
    },
    "ecmp-hash-key": {
      "layer4": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "False",
        "vipVariableName": "vpn_layer4"
      }
    },
    "nat64-global": {
      "prefix": {
        "stateful": {}
      }
    },
    "nat64": {
      "v4": {
        "pool": {
          "vipType": "ignore",
          "vipValue": [],
          "vipObjectType": "tree",
          "vipPrimaryKey": [
            "name"
          ]
        }
      }
    },
    "tenant-vpn-id": {},
    "org-name": {},
    "omp-admin-distance-ipv4": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_omp-admin-distance-ipv4"
    },
    "omp-admin-distance-ipv6": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_omp-admin-distance-ipv6"
    },
    "nat": {
      "natpool": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "name"
        ]
      },
      "port-forward": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "source-port",
          "translate-port",
          "source-ip",
          "translate-ip",
          "proto"
        ]
      },
      "static": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "source-ip",
          "translate-ip"
        ]
      },
      "subnet-static": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "source-ip-subnet",
          "translate-ip-subnet"
        ]
      }
    },
    "route-import-from": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "protocol",
        "source-vpn"
      ]
    },
    "dns": {
      "vipType": "constant",
      "vipValue": [
        {
          "role": {
            "vipType": "constant",
            "vipValue": "primary",
            "vipObjectType": "object"
          },
          "dns-addr": {
            "vipType": "constant",
            "vipValue": "8.8.8.8",
            "vipObjectType": "object"
          },
          "priority-order": [
            "dns-addr",
            "role"
          ]
        },
        {
          "role": {
            "vipType": "constant",
            "vipValue": "secondary",
            "vipObjectType": "object"
          },
          "dns-addr": {
            "vipType": "constant",
            "vipValue": "1.1.1.1",
            "vipObjectType": "object"
          },
          "priority-order": [
            "dns-addr",
            "role"
          ]
        }
      ],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "dns-addr"
      ]
    },
    "route-import": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "protocol"
      ]
    },
    "route-export": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "protocol"
      ]
    },
    "host": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "hostname"
      ]
    },
    "service": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "svc-type"
      ]
    },
    "ip": {
      "gre-route": {},
      "ipsec-route": {},
      "service-route": {}
    },
    "ipv6": {},
    "omp": {
      "advertise": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "protocol"
        ]
      },
      "ipv6-advertise": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "protocol"
        ]
      }
    }
  }
}
"""

subinterface_template = """
{
  "templateName": "~~~templateName~~~",
  "templateDescription": "~~~templateDescription~~~",
  "templateType": "cisco_vpn_interface",
  "deviceType": [
    "vedge-C8000V"
  ],
  "factoryDefault": false,
  "devicesAttached": 0,
  "attachedMastersCount": 0,
  "templateMinVersion": "15.0.0",
  "configType": "xml",
  "resourceGroup": "global",
  "templateDefinition": {
    "if-name": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": "~~~vpn_if_name~~~",
      "vipVariableName": "vpn_if_name"
    },
    "description": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": "~~~vpn_if_description~~~",
      "vipVariableName": "vpn_if_description"
    },
    "ip": {
      "address": {
        "vipObjectType": "object",
        "vipType": "constant",
        "vipValue": "~~~if_ip_address~~~",
        "vipVariableName": "if_ip_address"
      },
      "secondary-address": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      }
    },
    "dhcp-helper": {
      "vipObjectType": "list",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_dhcp_helper"
    },
    "flow-control": {},
    "clear-dont-fragment": {},
    "pmtu": {},
    "mtu": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": 1496,
      "vipVariableName": "vpn_if_ip_mtu"
    },
    "static-ingress-qos": {},
    "tcp-mss-adjust": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tcp_mss_adjust"
    },
    "mac-address": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_mac_address"
    },
    "speed": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_speed"
    },
    "duplex": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_duplex"
    },
    "shutdown": {
      "vipObjectType": "object",
      "vipType": "constant",
      "vipValue": "false",
      "vipVariableName": "vpn_if_shutdown"
    },
    "arp-timeout": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 1200,
      "vipVariableName": "vpn_if_arp_timeout"
    },
    "autonegotiate": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_autonegotiate"
    },
    "shaping-rate": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "rewrite_shaping_rate"
    },
    "qos-map": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "qos_map"
    },
    "qos-map-vpn": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn-qos_map"
    },
    "tracker": {
      "vipObjectType": "list",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tracker"
    },
    "bandwidth-upstream": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_bandwidth_upstream"
    },
    "bandwidth-downstream": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_bandwidth_downstream"
    },
    "block-non-source-ip": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "False",
      "vipVariableName": "vpn_if_block_non_source_ip"
    },
    "rewrite-rule": {
      "rule-name": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "rewrite_rule_name"
      }
    },
    "tloc-extension": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipVariableName": "vpn_if_tloc_extension"
    },
    "load-interval": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 30,
      "vipVariableName": "vpn_if_load_interval"
    },
    "icmp-redirect-disable": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "True",
      "vipVariableName": "vpn_if_icmp_redirect_disable"
    },
    "tloc-extension-gre-from": {
      "src-ip": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tloc-ext_gre_from_src_ip"
      },
      "xconnect": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipVariableName": "vpn_if_tloc-ext_gre_from_xconnect"
      }
    },
    "access-list": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "direction"
      ]
    },
    "auto-bandwidth-detect": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "False",
      "vipVariableName": "vpn_if_auto_bandwidth_detect"
    },
    "iperf-server": {
      "vipObjectType": "object",
      "vipType": "ignore"
    },
    "media-type": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "_empty",
      "vipVariableName": "vpn_if_media-type"
    },
    "intrf-mtu": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": 1500,
      "vipVariableName": "vpn_if_intrf_mtu"
    },
    "ip-directed-broadcast": {
      "vipObjectType": "object",
      "vipType": "ignore",
      "vipValue": "False",
      "vipVariableName": "vpn_if_ip-directed-broadcast"
    },
    "trustsec": {
      "enforcement": {
        "enable": {
          "vipObjectType": "object",
          "vipType": "ignore"
        },
        "sgt": {
          "vipObjectType": "object",
          "vipType": "ignore",
          "vipVariableName": "trusted_enforcement_sgt"
        }
      }
    },
    "ipv6": {
      "access-list": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "direction"
        ]
      },
      "address": {
        "vipObjectType": "object",
        "vipType": "ignore",
        "vipValue": "",
        "vipVariableName": "vpn_if_ipv6_ipv6_address"
      },
      "dhcp-helper-v6": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      },
      "secondary-address": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "address"
        ]
      }
    },
    "arp": {
      "ip": {
        "vipType": "ignore",
        "vipValue": [],
        "vipObjectType": "tree",
        "vipPrimaryKey": [
          "addr"
        ]
      }
    },
    "vrrp": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "grp-id"
      ]
    },
    "ipv6-vrrp": {
      "vipType": "ignore",
      "vipValue": [],
      "vipObjectType": "tree",
      "vipPrimaryKey": [
        "grp-id"
      ]
    }
  }
}
"""