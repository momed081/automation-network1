# paramiko script to configure some loopback interfaces
import paramiko  #ssh
import time
import getpass # hide password when input

uname = input("Username: ") or "cisco" # input username
passwd = getpass.getpass() or "cisco"

ssh_client = paramiko.SSHClient() 
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

#NESTED LIST
list_ip = [
        "192.168.122.62",
        "192.168.122.68"
    ]

for ip in list_ip:
    router_split = ip.split(".")[-1]
                                   
    ssh_client.connect(
        hostname=ip, 
        username=uname, 
        password=passwd
    )
    print("**********************************************")
    print(f"Success login to {ip}")
    conn = ssh_client.invoke_shell()
  
    #config shell cisco
    conn.send("configure terminal\n")

    for x in range(6, 9): #create looping for many interfaces according to range
        conn.send(f"interface lo{x}\n")
        conn.send(f"ip address 11.{x+1}.1.{router_split} 255.255.255.255\n") #IP Addr=interface + 1
        time.sleep(2) 

    conn.send("do write\n") # save configuration
    time.sleep(2)
    conn.send("do show ip int br | ex unas\n") #do show ip interface brief | exclude unassigned
    time.sleep(1)

    output = conn.recv(65535).decode() 
    print(output)

    ssh_client.close() 
