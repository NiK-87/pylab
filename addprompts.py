#Week 2 Exercise 1

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
	'host': 'cisco4.lasthop.io',
	'username': 'pyclass',
	'password': getpass(),
	'device_type': 'cisco_ios'
}

device2 = {
	'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type': 'cisco_ios',
	'global_delay_factor': 2
}


###PART A

#net_connect = ConnectHandler(**device1)
#command = 'ping'
#ping_response = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('8.8.8.8', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command_timing('\n', strip_prompt=False, strip_command=False)

#print(ping_response)

#net_connect.disconnect()


###PART B
#net_connect = ConnectHandler(**device1)
#command = 'ping'
#ping_response = net_connect.send_command(command, expect_string=r'ip', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('\n', expect_string=r'address', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('8.8.8.8', expect_string=r'count', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('\n', expect_string=r'size', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('\n', expect_string=r'seconds', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('\n', expect_string=r'commands', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('\n', expect_string=r'sizes', strip_prompt=False, strip_command=False)
#ping_response += net_connect.send_command('\n', expect_string=r'#', strip_prompt=False, strip_command=False)

#print(ping_response)

#net_connect.disconnect()


##Part 2
net_connect = ConnectHandler(**device2)
start_time = datetime.now()
output = net_connect.send_command_timing('show lldp neighbors detail')
end_time = datetime.now()
print(output)
print('Execution Time: {}'.format(end_time - start_time))
print()

start_time = datetime.now()
output = net_connect.send_command('show lldp neighbors detail', expect_string=r'#',delay_factor=8)
end_time = datetime.now()
print(output)
print('Execution Time: {}'.format(end_time - start_time))
print()

