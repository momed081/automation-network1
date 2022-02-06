# script for create 8 VLAN on multiple switches vie protocol telnet
import getpass
import telnetlib

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

f = open ('hosts') #file contain ip adress of multiple switches

for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
   # for n in range (2,31):
   #      tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
   #      tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN_4\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name Python_VLAN_5\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 6\n")
    tn.write(b"name Python_VLAN_6\n")
    tn.write(b"vlan 7\n")
    tn.write(b"name Python_VLAN_7\n")
    tn.write(b"vlan 8\n")
    tn.write(b"name Python_VLAN_8\n")
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
