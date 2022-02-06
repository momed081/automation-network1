#netmiko script to config multiple devices with 2 different commands files
# connection via ssh
from netmiko import ConnectHandler

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.63',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.64',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.65',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.66',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.67',
    'username': 'cisco',
    'password': 'cisco',
}

with open('commands') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('commands2') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s6, iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
