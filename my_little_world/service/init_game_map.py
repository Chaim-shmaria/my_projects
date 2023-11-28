import settings
from entities import employment
from map_view import MapView

employments = employment.employments_group()
map = MapView()


def init_game_map():
    for employ in employments:
        employ.position = map.select_random_position()
        map.insert_object(employ, employ.pos)  # maybe should reduce the pos argument from func


# for i in range(settings.INITIAL_BUILDINGS_NUM):



print(employments)