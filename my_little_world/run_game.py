import pygame
from images.images import GameGallery
from settings import Settings
from service.handle_keys import key_event
import keyboard

SCREEN_WIDTH = Settings().window_width
SCREEN_HEIGHT = Settings().window_height


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("MY little perfect world")
        self.clock = pygame.time.Clock()
        self.images = GameGallery()
        self.running = True

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            keyboard.hook(key_event)

    def update(self):
        pass

    def draw(self):
        pass

    def run_loop(self):
        while self.running:
            self.handle_inputs()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)  # Limit to 60 frames per second


if __name__ == "__main__":
    game = Game()
    game.run_loop()
    pygame.quit()
    quit()
