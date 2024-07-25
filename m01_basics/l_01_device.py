from pprint import pprint

# Dictionary representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nsox",
    "version": "9.3.(3)",
    "ip": "10.1.1.1"
}

# Simple Print
print("\n_____ SIMPLE PRINT ____________________")
print("device: ",  device)
print("device name:", device["name"])

# PRETTY Print
print("\n_____ PRETTY PRINT ____________________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n_______ FOR LOOP, USING F-STRING ______")
for key, value in device.items():
    print(f"{key:>16s} : {value}")
