from ..images.images import GameGallery

gallery = GameGallery()


class Recreation:
    def __init__(self):
        self.images = gallery.src_to_img(gallery.recreation)
        self.image = self.images[self]


class Restaurant(Recreation):
    pass


class Soccer(Recreation):
    pass


class Pool(Recreation):
    pass


class Bar(Recreation):
    pass


class Library(Recreation):
    pass


class Park(Recreation):
    pass


class Playground(Recreation):
    pass
