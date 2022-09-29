vpnStart = 2000
vpnEnd = 2299
deviceType = 'vedge-C8000V'

cliTemplate = '''system
 system-ip             {{system_ip}}
 overlay-id            1
 site-id               {{site_id}}
 region                {{region}}
 no transport-gateway enable
 port-offset           0
 control-session-pps   300
 admin-tech-on-failure
 sp-organization-name  atlnrlab
 organization-name     atlnrlab
 port-hop
 track-transport
 track-default-gateway
 console-baud-rate     9600
 no on-demand enable
 on-demand idle-timeout 10
 vbond 192.168.1.84 port 12346
!
banner login \\x03Un authorised Logins tracked\\x03
banner motd \\x03Restricted Use\\x03
service timestamps debug datetime msec
service timestamps log datetime msec
service tcp-keepalives-in
service tcp-keepalives-out
no service tcp-small-servers
no service udp-small-servers
platform console serial
hostname {{hostname}}
username admin privilege 15 secret 9 $9$3V6L3V6L2VUI2k$ysPnXOdg8RLj9KgMdmfHdSHkdaMmiHzGaUpcqH6pfTo
~~~vrf-definitions~~~
vrf definition Mgmt-intf
 description Management VPN
 rd          1:512
 address-family ipv4
  route-target export 1:512
  route-target import 1:512
  exit-address-family
 !
 address-family ipv6
  exit-address-family
 !
!
ip arp proxy disable
no ip finger
no ip rcmd rcp-enable
no ip rcmd rsh-enable
no ip dhcp use class
ip name-server 8.8.8.8
~~~vrf-name-servers~~~
ip name-server vrf Mgmt-intf 8.8.8.8
ip bootp server
no ip source-route
no ip http server
no ip http secure-server
ip nat settings central-policy
ipv6 unicast-routing
ipv6 rip vrf-mode enable
cdp run
interface GigabitEthernet1
 description   Management Interface
 no shutdown
 arp timeout 1200
 vrf forwarding Mgmt-intf
 ip address dhcp client-id GigabitEthernet1
 no ip redirects
 ip dhcp client default-router distance 1
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet2
 description   Internet
 no shutdown
 arp timeout 1200
 ip address dhcp client-id GigabitEthernet2
 no ip redirects
 ip dhcp client default-router distance 1
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
interface GigabitEthernet3
 no shutdown
 arp timeout 1200
 no ip redirects
 ip mtu    1500
 load-interval 30
 mtu           1500
 negotiation auto
exit
~~~subinterfaces~~~
interface GigabitEthernet4
 no shutdown
exit
interface Tunnel2
 no shutdown
 ip unnumbered GigabitEthernet2
 no ip redirects
 ipv6 unnumbered GigabitEthernet2
 no ipv6 redirects
 tunnel source GigabitEthernet2
 tunnel mode sdwan
exit
control-plane
!
clock timezone UTC 0 0
logging persistent size 104857600 filesize 10485760
no logging monitor
logging buffered 512000
logging console
aaa authentication login default local
aaa authorization exec default local
aaa server radius dynamic-author
!
snmp-server ifindex persist
line aux 0
 stopbits 1
!
line con 0
 speed    9600
 stopbits 1
!
line vty 0 4
 transport input ssh
!
line vty 5 80
 transport input ssh
!
lldp run
nat64 translation timeout tcp 3600
nat64 translation timeout udp 300
sdwan
 interface GigabitEthernet2
  tunnel-interface
   encapsulation ipsec weight 1
   no border
   color biz-internet restrict
   no last-resort-circuit
   no low-bandwidth-link
   no vbond-as-stun-server
   vmanage-connection-preference 5
   port-hop
   carrier                       default
   nat-refresh-interval          5
   hello-interval                1000
   hello-tolerance               12
   no allow-service all
   no allow-service bgp
   allow-service dhcp
   allow-service dns
   allow-service icmp
   allow-service sshd
   no allow-service netconf
   no allow-service ntp
   no allow-service ospf
   no allow-service stun
   allow-service https
   no allow-service snmp
   no allow-service bfd
  exit
 exit
 interface GigabitEthernet3
 exit
 appqoe
  no tcpopt enable
  no dreopt enable
  no httpopt enable
 !
 omp
  no shutdown
  send-path-limit  4
  ecmp-limit       4
  graceful-restart
  no as-dot-notation
  timers
   holdtime               60
   advertisement-interval 1
   graceful-restart-timer 43200
   eor-timer              300
  exit
  address-family ipv4
   advertise bgp
   advertise connected
   advertise static
  !
  address-family ipv6
   advertise bgp
   advertise connected
   advertise static
  !
 !
!
bfd color lte
 hello-interval 1000
 no pmtu-discovery
 multiplier     1
!
bfd default-dscp 48
bfd app-route multiplier 2
bfd app-route poll-interval 123400
security
 ipsec
  rekey          86400
  replay-window  512
  integrity-type ip-udp-esp esp
 !
!
sslproxy
 no enable
 rsa-key-modulus      2048
 certificate-lifetime 730
 eckey-type           P256
 ca-tp-label          PROXY-SIGNING-CA
 settings expired-certificate  drop
 settings untrusted-certificate drop
 settings unknown-status       drop
 settings certificate-revocation-check none
 settings unsupported-protocol-versions drop
 settings unsupported-cipher-suites drop
 settings failure-mode         close
 settings minimum-tls-ver      TLSv1
 dual-side optimization enable
!
'''

