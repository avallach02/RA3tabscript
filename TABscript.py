import pydirectinput
import keyboard

max_tabs = 10
current_tab = 0
print("Читы запущены, ну ты и пид*** конечно)")

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'tab':
            current_tab += 1

            if current_tab > max_tabs:
                current_tab = 1

            pydirectinput.press(f"f{current_tab}")
            if current_tab == max_tabs:
                current_tab = 0

        elif event.name in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            current_tab = 0