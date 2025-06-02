"""
Command Design Pattern: This module defines the command interface and concrete command classes.
"""

from typing import Protocol


class ICommand(Protocol):
    """
    Command interface that defines the execute method.
    """

    def execute(self) -> None:
        """
        Execute the command.
        """
        pass

    def undo(self) -> None:
        """
        Undo the command.
        """
        pass


class LightCommand(ICommand):
    """
    Command to control the light.
    """

    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        print(self.light.on())

    def undo(self) -> None:
        print(self.light.off())


class FanCommand(ICommand):
    """
    Command to control the fan.
    """

    def __init__(self, fan):
        self.fan = fan

    def execute(self) -> None:
        print(self.fan.on())

    def undo(self) -> None:
        print(self.fan.off())
