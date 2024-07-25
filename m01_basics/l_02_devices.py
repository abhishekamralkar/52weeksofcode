from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list() # CREATE EMPTY LIST FOR HOLDING DEVICES

# FOR LOOP TO CREATE LARGE NUMBER OF DEVICES
for index in range(1,10):

    # CREATE DEVICE DICTIONARY
    device = dict()

    # RANDOM DEVICE NAME

    device["name"] = (
        choice(["r1", "r2", "r3", "r4"])
        + choice(["L", "U"])
        + choice(string.ascii_letters))

    device["vendor"] = choice(["cisco", "juniper", "arista"])
    
    if device["vendor"] == "cisco":
        device["os"] = "nexus"
        device["version"] = choice(["18.09", "19.09", "20.09"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["18.09", "19.09", "20.09"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["20.10", "21.10", "22.10"])
    device["ip"] = "10.0.0." + str(index)
    
    # NICELY FORMATTED PRINT OF DEVICES
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # ADD ALL DEVICES TO THE LIST OF DEVICES
    devices.append(device)

# USE PPRINT TO PRINT DEVICES
print("\n________ DEVICES AS LIST OF DICTS _______________")
pprint(devices)

# USE TABULATE TO PRINT TABLE OF DEVICES
print("\n_________ SORTED DEVICES IN TABULAR FORMAT _________")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
