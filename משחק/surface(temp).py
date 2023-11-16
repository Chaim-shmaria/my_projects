import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

# Constants
HTW = 36
HTH = 18
GRID_WIDTH = 10
GRID_HEIGHT = 10
TILE_SIZE = 3
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 620

# Initialize Pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Isometric Grid Example')

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# View class
class View:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0

    def project(self, location):
        x = (location[0] - location[1]) * HTW + self.offset_x
        y = (location[0] + location[1]) * HTH  + self.offset_y
        return pygame.Vector2(x + WINDOW_WIDTH / 2, y + WINDOW_HEIGHT / 2)

# Grid class
class Grid:
    def draw(self, view):
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                x = col * TILE_SIZE
                y = row * TILE_SIZE
                tile_color = WHITE if (row + col) % 2 == 0 else GRAY
                pygame.draw.polygon(window, tile_color, [
                    view.project([x, y, 0]),
                    view.project([x + TILE_SIZE, y]),
                    view.project([x + TILE_SIZE, y + TILE_SIZE]),
                    view.project([x, y + TILE_SIZE])
                ])

# Create a grid
grid = Grid()

# Create the view
view = View()

# Main game loop
while True:
    window.fill((135, 206, 250))  # Sky color

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        view.offset_x += 10
    if keys[K_RIGHT]:
        view.offset_x -= 10
    if keys[K_UP]:
        view.offset_y += 10
    if keys[K_DOWN]:
        view.offset_y -= 10

    grid.draw(view)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
