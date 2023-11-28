import settings
import random


class MapView:
    def __init__(self):
        self.map_width = settings.MAP_WIDTH
        self.map_height = settings.MAP_HEIGHT

        self.display_matrix = [[[0] * self.map_width for _ in range(self.map_height)] for _ in range(3)]
        self.camera_position_x = 0
        self.camera_position_y = 0
        self.empty_positions = []

    def insert_object(self, _object, position):  # maybe we can reduce the position argument
        x, y, z = position
        self.display_matrix[x][y][z] = _object
        self.empty_positions.append((x, y, z))

    def remove_object(self, position):
        x, y, z = position
        self.display_matrix[x][y][z] = 0
        self.empty_positions.remove((x, y, z))

    def move_camera(self, direction):
        if direction == 'right':
            self.camera_position_x += 5
        if direction == 'left':
            self.camera_position_x -= 5
        if direction == 'up':
            self.camera_position_y -= 5
        if direction == 'down':
            self.camera_position_y += 5

    def display(self, screen):
        for dim in self.display_matrix:
            for row in dim:
                for dispalyed_object in row:
                    screen.blit(dispalyed_object,
                                dispalyed_object.position)  # object need to have position attribute or something...

    def select_random_position(self):
        position = random.choice(self.empty_positions)


# a = Display(3, 3)
# for r in a.display_matrix:
#     for j in r:
#         print(j)
#     print('\n')
