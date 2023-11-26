# Mediates input readings from the controller, relays them to the model, and returns the corresponding view

from model.pygame_functions import PygameFunctions
from model.images import GameGallery


class Executor:
    def __init__(self):
        self.pygame_functions = PygameFunctions()
        self.pygame_functions.init_pygame()
        self.pygame_functions.init_screen()
        self.pygame_functions.run_loop()
        # here need to add the call to display method
        self.images = GameGallery()

    def handle_keys(self, key):
        self.pygame_functions.handle_keys(key)

    # looks like we have to add moving inputs func. and mouse input. and other kind inputs functions.
    # not just one func "handle_keys"...




