from ..images.images import GameGallery


# gallery = GameGallery()


class House:
    def __init__(self, pos):
        self.image = None
        self.position = pos
        self.Tenants = []
        self.content = []
        self.image = GameGallery().src_to_img(GameGallery().house, self)
