from pprint import pprint
from random import choice
import copy

from util.create_utils import create_network

device = {
    "name": "r3-L-n7",
    "vendor": "cisco",
    "model": "catalyst 2968",
    "os": "ios",
    "interfaces": [
        ]
}

print("\n\n----- device with no interfaces-------")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

interfaces = list()
for index in range(0, 8):
    interface = {
        "name": "g/0/0/" + str(index),
        "speed": choice(["10", "100", "1000"])
    }
    interfaces.append(interface)

device["interfaces"] = interfaces

print("\n\n----- device with interfaces-----------")
for key, value in device.items():
    if key != "interfaces":
        print(f"{key:>16s} : {value}")
    else:
        print(f"{key:>16s} :")
        for interface in interfaces:
            print(f"\t\t\t\t\t{interface}")

print()
print("\n\n----- device with interfaces using pprint-------------")
pprint(device)

print("\n\n----- network with devices and interfaces---------")
network = create_network(num_devices=4, num_subnets=4)
pprint(network)

print("\n----- information about network--------")
print(f"-----number of subnets: {len(network['subnets'])}")
print(f"---list of subnets: {network['subnets'].keys()}")
print(f"---list of subnets w/o extraneous: {', '.join(network['subnets'])}")
