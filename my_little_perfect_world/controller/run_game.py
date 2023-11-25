import keyboard
from view.executor import Executor


def key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        Executor().handle_keys(e.name)  # need to set it well


# need to add the mouse input function

executor = Executor()

keyboard.hook(key_event)

quit()
