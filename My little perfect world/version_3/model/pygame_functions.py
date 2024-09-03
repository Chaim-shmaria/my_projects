import pygame
from controller.settings import Settings

SCREEN_WIDTH = Settings().window_width
SCREEN_HEIGHT = Settings().window_height


class PygameFunctions:
    def __init__(self):
        self.running = None

    def init_pygame(self):
        pygame.init()

    def init_screen(self):
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MY little perfect world")

    def handle_keys(self, key=None):
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

    def game_maintenance(self):
        pass

    def run_loop(self):
        running = True
        while running:
            self.handle_keys()
            self.game_maintenance()
