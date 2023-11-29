import settings
from entities import employment
from service.map_view import MapView

initial_builddings_amount = settings.INITIAL_BUILDINGS_AMOUNT

employments = employment.employments_group()
MAP = MapView()


def init_game_map():
    for employ in employments:
        employ.position = MAP.select_random_position()
        MAP.insert_object(employ)


init_game_map()
for i in employments:
    print(i.position)
