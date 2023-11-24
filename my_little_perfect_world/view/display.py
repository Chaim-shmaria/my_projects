class Display:
    def __init__(self, map_width, map_height):
        self.display_matrix = [[[0] * map_width for _ in range(map_height)] for _ in range(3)]
        self.camera_place_x = 0
        self.camera_place_y = 0

    def insert(self, object, pos):  # maybe we can reduce the pos argument
        x, y, z = pos
        self.display_matrix[x][y][z] = object

    def remove(self, pos):
        x, y, z = pos
        self.display_matrix[x][y][z] = 0

    def move_camera(self, direction):
        if direction == 'right':
            self.camera_place_x += 5
        if direction == 'left':
            self.camera_place_x -= 5
        if direction == 'up':
            self.camera_place_y -= 5
        if direction == 'down':
            self.camera_place_y += 5

    def display(self, screen):
        for dim in self.display_matrix:
            for row in dim:
                for element in row:
                    screen.blit(element, element.pos)  # object need to have pos attribute or something...


# a = Display(3, 3)
# for r in a.display_matrix:
#     for j in r:
#         print(j)
#     print('\n')
