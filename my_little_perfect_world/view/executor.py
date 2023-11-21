import pygame
from controller.settings import Settings


SCREEN_WIDTH = Settings().window_width
SCREEN_HEIGHT = Settings().window_height


class Executor:
    def __init__(self):
        self.screen = None
        self.running = None


    def initialize_game_interface(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MY little perfect world")
        self.running = True


    def initialize_variables(self):
        pass

    def run_game(self):
        while self.running:
            self.game_maintenance()

    def game_maintenance(self):
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

    def quit(self):
        pygame.quit()
