from tabulate import tabulate
from util import create_devices

# ------- MAIN PROGRAM --------------------
if __name__ == "__main__":

    devices = create_devices(num_subnets=5, num_devices=4)
    print("\n", tabulate(devices, headers="keys"))