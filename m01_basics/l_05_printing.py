from l_03_functions import create_devices
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice
import nmap

devices = create_devices(25)

print("\n\nUSING PRINT")
print(devices)

print("\n\nUSING PPRINT")
pprint(devices)

print("\n\nUSING LOOP")
for device in devices:
    sleep(0.1)
    device["last_heard"] = str(datetime.now())
    print(device)

print("\n\nUSING TABULATE")
print(
    tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys")
)

print("\n\nUSING LOOP AND F-STRING")
print("   NAME     VENDOR : OS    IP ADDRESS      LAST HEARD")
print("   -----    -------  ---   ------------    ----------")
for device in devices:
    print(
        f'{device["name"]:>7} {device["vendor"]:>10} {device["os"]:<6}  {device["ip"]:<6} {device["last_heard"][:-4]}'
    )

print("\nSame thing, but sorted descending by last_haerd")
for device in sorted(devices, key=itemgetter("last_heard"), reverse=True):
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}  {device["last_heard"][:-4]}'
    )

print("\n\nMULTIPLE PRINT STATEMENTS, SAME LINE")
print("Testing Devices")
for device in devices:
    print(f'--- testing device {device["name"]} ...', end="")
    sleep(choice([0.1, 0.2, 0.3, 0.4]))
    print("done.")
print("Testing completed")

nm = nmap.PortScanner()
while True:

    ip = input("\nInput IP ADDRESS to scan: ")
    if not ip:
        break

    print(f"\n--- beginning scan of {ip}")
    output = nm.scan(ip, '22-1024')
    print(f"--- --- command: {nm.command_line()}")

    print("----- nmap scan output ------------------")
    pprint(output)
