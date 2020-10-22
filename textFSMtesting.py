import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint


password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device1 = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'device_type': 'cisco_ios'
}

net_connect = ConnectHandler(**device1)

print()

cmds = ['show version', 'show lldp neighbors']

for cmd in cmds:
	output = net_connect.send_command(cmd, use_textfsm=True)
	print('#'*20)
	print(cmd)
	print('#'*20)
	pprint(output)
	print('#'*20)
	print()

	if cmd == 'show lldp neighbors':
		print('LLDP Data Structure Type: {}'.format(type(output)))
		print('HPE Switch Connection Port: {}'.format(output[0]['neighbor_interface']))

print()
net_connect.disconnect()
