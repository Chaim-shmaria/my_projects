import pygame
import settings
from entities import employment
from service.map_view import MapView
from images.images import GameGallery

initial_buildings_amount = settings.INITIAL_BUILDINGS_AMOUNT
MAP = MapView()


# combine entities and their images
employments = employment.employments_group()
for employment in employments:
    employment.image = pygame.image.load(GameGallery().employment[f'{employment}'])





def init_game_map():
    for employ in employments:
        #  select positions (=random) for all initial buildings
        employ.position = MAP.select_random_position()
        MAP.insert_object(employ)


init_game_map()
for i in employments:
    print(i.position)
