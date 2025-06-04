from facade_pattern.subsystems import CPU, RAM, HardDrive, PowerSupply


class Facade:
    def __init__(self, power_supply: PowerSupply, cpu: CPU, ram: RAM, hard_drive: HardDrive):
        self._power_supply = power_supply
        self._cpu = cpu
        self._ram = ram 
        self._hard_drive = hard_drive 

    def perform_operations(self):
        self._power_supply.turn_on()
        self._cpu.freeze()
        self._ram.load(0)
        self._hard_drive.read(0, 1024)
        self._hard_drive.write(0)
        self._ram.unload(0)
        self._cpu.execute()
        self._power_supply.turn_off()        