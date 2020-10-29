import re
import os
import yaml
import json
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pprint import pprint



filename = "json.txt"

with open(filename) as file:
	nxos_data = json.load(file)


ipv4_list = []
ipv6_list = []


for intf, ipaddr_dict in nxos_data.items():
	for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
		for ip_addr, prefix_dict in addr_info.items():
			prefix_length = prefix_dict["prefix_length"]
			if ipv4_or_ipv6 == "ipv4":
				ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
			elif ipv4_or_ipv6 == "ipv6":
				ipv6_list.append("{}/{}".format(ip_addr, prefix_length))


print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))


