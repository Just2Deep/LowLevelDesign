

class PowerSupply:
    def turn_on(self):
        print("Power supply turned on.")

    def turn_off(self):
        print("Power supply turned off.")

class CPU:
    def freeze(self):
        print("CPU frozen.")

    def jump(self, position):
        print(f"Jumping to {position}.")

    def execute(self):
        print("Executing CPU instructions.")

class RAM:
    def load(self, position):
        print(f"Loading data into RAM at {position}.")

    def unload(self, position):
        print(f"Unloading data from RAM at {position}.")

class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from hard drive at LBA {lba}.")
        return "data"

    def write(self, lba):
        print(f"Writing data to hard drive at LBA {lba}.")