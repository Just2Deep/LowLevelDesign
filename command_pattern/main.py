from command_pattern.command import LightCommand, FanCommand
from command_pattern.devices import Light, Fan
from command_pattern.remote_control import RemoteControl


def main():
    living_room_light = Light(name="Living Room Light")
    ceiling_fan = Fan(name="Ceiling Fan")

    remote = RemoteControl()

    remote.set_command(0, LightCommand(living_room_light))
    remote.set_command(1, FanCommand(ceiling_fan))

    # Toggling light
    remote.press_button(0)  # Turn on the light
    remote.press_button(0)  # Turn off the light

    # Toggling fan
    remote.press_button(1)  # Turn on the fan
    remote.press_button(1)  # Turn off the fan

    # Attempting to press an invalid button
    try:
        remote.press_button(2)  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
