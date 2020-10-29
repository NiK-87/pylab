import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

#6. Use Netmiko to retrieve 'show run' from the Cisco4 device. 
#Feed this configuration into CiscoConfParse.
#
#Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. 
#Print out the interface name and IP address for each interface. 
#Your solution should work if there is more than one IP address configured on Cisco4. 
#For example, if you configure a loopback interface on Cisco4 with an IP address, 
#then your solution should continue to work. The output from this program should 
#look similar to the following:
#$ python confparse_ex6.py 
#
#Interface Line: interface GigabitEthernet0/0/0
#IP Address Line:  ip address 10.220.88.23 255.255.255.0






if __name__ == "__main__":
	home_dir = path.expanduser("~")
	filename = path.join(home_dir, ".netmiko.yml")

	with open(filename) as f:
		yaml_out = yaml.safe_load(f)

	device = yaml_out["cisco4"]
	net_connect = ConnectHandler(**device)
	show_run = net_connect.send_command("show run")
	
	#When feeding config direct, confparse requires a list
	cisco_cfg = CiscoConfParse(show_run.splitlines())
	interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface",childspec=r"^\s+ip address")
	

	print()
	for intf in interfaces:
		print("Interface Line: {}".format(intf.text))
		ip_address = intf.re_search_children(r"ip address")[0].text
		print("IP Address Line: {}".format(ip_address))
		print()

	print()
