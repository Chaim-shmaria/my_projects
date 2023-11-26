from model.images import GameGallery


recreation_images = GameGallery().recreation


class Recreation:
    def __init__(self):
        self.image = GameGallery().src_to_img(recreation_images, f"{self}")


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
