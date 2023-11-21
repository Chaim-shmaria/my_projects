from ..images.images import GameGallery


# gallery = GameGallery()


class Recreation:
    def __init__(self):
        self.image = GameGallery().src_to_img(GameGallery().recreation, self)


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
