from command_pattern.command import ICommand


class RemoteControl:
    def __init__(self):
        from typing import Optional

        self.num_of_buttons = 4
        self.buttons: list[Optional[ICommand]] = [None] * self.num_of_buttons
        self.buttons_pressed = [False] * self.num_of_buttons

    def set_command(self, button: int, command: ICommand):
        if button < 0 or button >= self.num_of_buttons:
            raise ValueError("Invalid button")

        if self.buttons[button] is not None:
            del self.buttons[button]

        self.buttons[button] = command
        self.buttons_pressed[button] = False

    def press_button(self, button: int):
        if (
            0 <= button < self.num_of_buttons
            and self.buttons[button] is not None
            and isinstance(self.buttons[button], ICommand)
        ):
            if not self.buttons_pressed[button]:
                self.buttons[button].execute()
                self.buttons_pressed[button] = True
            else:
                self.buttons[button].undo()
                self.buttons_pressed[button] = False
        else:
            raise ValueError("Unknown command")
