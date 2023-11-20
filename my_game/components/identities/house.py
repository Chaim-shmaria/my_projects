from ..images.images import GameGallery

gallery = GameGallery()


class House:
    def __init__(self, pos):
        self.image = None
        self.position = pos
        self.Tenants = []
        self.content = []
        self.images = gallery.src_to_img(gallery.house)
        self.image = self.images[self]
