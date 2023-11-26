import keyboard
import pygame  # not sure if it necessary


def _handle_keys(key=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.K_UP:
            pass
        if event.type == pygame.K_RIGHT:
            pass
        if event.type == pygame.QUIT:
            pass
        if event.type == pygame.QUIT:
            pass
        # and more and more


def key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        return _handle_keys(e.name)  # need to set it well


# need to add the mouse input function

