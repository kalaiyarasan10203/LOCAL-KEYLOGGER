#!/usr/bin/env python
import subprocess
import optparse
import re
def change_mac(interface,new_mac):
    print("[+] Changing MAC address to new mac")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("i","interface", dest = "interface", help="To change the MAC address")
    parser.add_option("m","mac", dest= "new mac", help="Enter the new MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, usehelp for more info")
    elif not options.new_mac:
        parser.error("[-] please specify an MAC, use-help for more info")
        return options
options = get_arguments()    
change_mac(options.interface, options.new_mac)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
