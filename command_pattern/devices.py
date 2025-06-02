class Light:
    def __init__(self, name, state=False):
        self.name = name
        self.state = state

    def on(self):
        self.state = True
        return f"{self.name} is now on"

    def off(self):
        self.state = False
        return f"{self.name} is now off"

    def __str__(self):
        return f"Light(name={self.name}, state={'on' if self.state else 'off'})"


class Fan:
    def __init__(self, name):
        self.name = name

    def on(self):
        self.speed = 1
        return f"{self.name} is now on"

    def off(self):
        self.speed = 0
        return f"{self.name} is now off"

    def __str__(self):
        return f"Fan(name={self.name}, speed={self.speed})"
