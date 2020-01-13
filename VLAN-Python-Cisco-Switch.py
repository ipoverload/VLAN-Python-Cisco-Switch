#!/usr/bin/env python

import getpass
import sys
import telnetlib    

print("\nWARNING: THIS PROGRAM WORKS ONLY IF ALL THE DEVICES ARE USING SAME USER CREDENTIALS.")
print("THIS PROGRAM IS INTENDED TO BE USED WITH CISCO SWITCHES ONLY!\n")

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

if raw_input("\nAre you using same user credentials for all devices(y/n)?: \n") == 'y':

    switch_num = raw_input("\nEnter the number of Switches you want to configure: \n")
 
    switch_num1 = int(switch_num)
    x = switch_num1 + 1

    for n in range (1,x):

        ip_address = raw_input("\nEnter the IP address of Switch" + str(n) + ": \n")
 
        tn = telnetlib.Telnet(ip_address)        
 
        tn.read_until("Username: ")
        tn.write(user + "\n")

        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")        

        tn.write("conf t\n")

        vlan_no = raw_input("\nEnter the number of VLANs you want to create in Switch" + str(n) + ": \n")
        
        y = int(vlan_no)
        
        if y > 0:
        
            vlan_name = raw_input("\nEnter the vlan name prefix for all VLANs of Switch" + str(n) + ": \n")
            print("\nINFO: VLANs will be created starting from VLAN number 2 since VLAN 1 is native VLAN by default in Cisco Switches\n")
            print("WARNING: Executing Python Script... Do not press any key until prompted. Please wait...")
            print ("Configuring Switch" + str(n) + "...")

            for a in range (2,y+2):
                tn.write("vlan " + str(a) + "\n")
                tn.write("name " + vlan_name + "_" + str(a) + "\n")
            tn.write("end\n")
            tn.write("exit\n")

            print tn.read_all()
            print ("Done Configuration for Switch" + str(n) + "!\n")

    print ("\nEnd of Python Script Execution\n")
