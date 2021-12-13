import winsound
from pynput.keyboard import Listener, Controller, Key
from utils import list_of_message, note_keys
from os import system




def pynotes_keylogger():
    # Definition zone

    keyboard = Controller() # Keyboard emulator

    info = {
        "duration": 300,  # milisecond
        "pitch_level": 2  # pitch level determine how high or how low the note is, using pitch level is easier than using a specific pitch of a note
    }

    def playsound(frequency):
        winsound.Beep(frequency * info['pitch_level'], info["duration"])



    # Main
    print("Welcome to pynotes! Press 'h' for help.\n")

    def on_press(key):
        try:
            key_code = key.vk

            if key_code in note_keys:
                print(f"Pressed {key}")
                playsound(note_keys[key_code])
                return

            match key_code:
                case 67:  # C
                    if not info["pitch_level"] - 1:
                        print(f"Lowest level of pitch reached: {info['pitch_level']}")
                        return
                    info["pitch_level"] = info["pitch_level"] - 1

                    print(f"Decreased pitch to level: {info['pitch_level']}")

                case 78:  # N
                    if info["pitch_level"] + 1 == 17:
                        print(f"Reached highest pitch possible: {info['pitch_level']}")
                        return

                    info["pitch_level"] = info["pitch_level"] + 1

                    print(f"Increased pitch to level: {info['pitch_level']}")

                case 86:  # V
                    if info["duration"] - 100 < 0:
                        print(f"Reached lowest duration possible: {info['duration']}ms")
                        return

                    info["duration"] = info["duration"] - 100

                    print(f"Decreased duration to: {info['duration']}ms")

                case 66:  # B
                    if info["duration"] + 100 > 15000:
                        print(f"Reached highest duration possible: {info['duration']}ms")
                        return

                    info["duration"] = info["duration"] + 100
                    print(f"Increased duration to: {info['duration']}ms")

                case 72:  # H

                    # clear the prompt's input when pressing 'h' because pynput still accepts text input when you pressed a key
                    keyboard.press(Key.esc)
                    system("cls")
                    for message in list_of_message:
                        print(message)
                        input("---See More---")

        except AttributeError:
            key_code = key.value.vk

            match key_code:
                case 46:  # Delete key
                    system("cls")

    listener = Listener(on_press=on_press)
    listener.start()

    try:
        while listener.is_alive():
            pass
    except KeyboardInterrupt:
        print("EXITED")
        listener.stop()

if __name__ == "__main__":
    pynotes_keylogger()