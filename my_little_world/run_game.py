import pygame
import settings
from images.images import GameGallery
from service.handle_keys import key_event
import keyboard
from service import init_game_map


class Game:
    def __init__(self):
        # load game surface:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("MY little perfect world")
        self.clock = pygame.time.Clock()
        self.running = True
        # load game tools:
        self.images = GameGallery()
        init_game_map()

    def click_by_keyboard(self):
        pass

    def click_by_mouse(self):
        pass

    def handle_inputs(self):
        for event in pygame.event.get():
            # close game:
            if event.type == pygame.QUIT:
                self.running = False
            # others:
            keyboard.hook(key_event)  # need to check usage
            self.click_by_keyboard()
            self.click_by_mouse()

    def update(self):
        pass

    def draw(self):
        pygame.display.flip()
        pygame.draw.rect(self.screen)  # temp line. so func won't be static...

    def run_loop(self):
        while self.running:
            self.handle_inputs()
            self.update()
            self.draw()
            self.clock.tick(60)  # Limit to 60 frames per second


if __name__ == "__main__":
    game = Game()
    game.run_loop()
    pygame.quit()
    quit()
