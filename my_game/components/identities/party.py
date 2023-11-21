from ..images.images import GameGallery

# gallery = GameGallery()


class Party:
    def __init__(self):
        self.members = []
        self.image = GameGallery().src_to_img(GameGallery().party, self)


class MusicClass(Party):
    pass


class YogaClass(Party):
    pass
