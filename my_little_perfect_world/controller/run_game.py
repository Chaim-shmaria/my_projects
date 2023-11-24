import keyboard
from view.executor import Executor


def key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        Executor().game_maintenance(e.name)  # need to set it well


# need to add the mouse input function

executor = Executor()

executor.run_game()

keyboard.hook(key_event)

quit()
