from facade_pattern.facade import Facade
from facade_pattern.subsystems import CPU, RAM, HardDrive, PowerSupply


class Client:
    def __init__(self, facade: Facade):
        self.facade = facade

    def run(self):
        print("Client: Invoking the facade to perform operations.")
        self.facade.perform_operations()
        print("Client: Operations completed.")

if __name__ == "__main__":
    power_supply = PowerSupply()
    cpu = CPU()
    ram = RAM()
    hard_drive = HardDrive()
    facade = Facade(power_supply, cpu, ram, hard_drive)
    client = Client(facade)
    client.run()