from ..images.images import GameGallery

gallery = GameGallery()


class Party:
    def __init__(self):
        self.members = []
        self.images = gallery.src_to_img(gallery.party)
        self.image = self.images[self]


class MusicClass(Party):
    pass


class YogaClass(Party):
    pass
