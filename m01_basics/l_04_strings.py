from pprint import pprint

device1_str = "  r3-L-n7, chhisco, catalyst 2960, ios   "

# SPLIT
print("STRING SPLIT, SPLIT REPLACE")
device1 = device1_str.split(",")
print("device1 using split")
print("    ", device1)

# STRIP
device1 = device1_str.strip().split(",")
print("device1 using split and strip:")
print("    ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n   ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks, comma to colon:")
print("   ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item")
print("   ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension")
print("   ", device1)

# IGNORING CASE
print("\n\nIGNOREING CASE")
model = "CSR1000V"
if model == "csr1000v":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

model = "CSR1000V"
if model.lower() == "csr1000v":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

# FINDING SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index}")
else:
    print(f"not found: {expected_version}")

# SEPARATING STRING COMPONENTS
print("\n\nSEPARATING VERSION STRING COMPONENTS")
version_info = version.split(",")
for version_info_part in version_info:
    print(f"version part: {version_info_part.strip()}")