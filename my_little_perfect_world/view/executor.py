import pygame
from controller.settings import Settings
from model.images import GameGallery

SCREEN_WIDTH = Settings().window_width
SCREEN_HEIGHT = Settings().window_height


class Executor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MY little perfect world")
        self.running = True
        self.images = GameGallery()

    def run_game(self):
        while self.running:
            self.game_maintenance()

    def game_maintenance(self, key):
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
