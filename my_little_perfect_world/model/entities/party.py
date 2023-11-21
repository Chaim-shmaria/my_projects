from service.images.images import GameGallery

party_images = GameGallery().party


class Party:
    def __init__(self):
        self.members = []
        self.image = GameGallery().src_to_img(party_images, f"{self}")


class MusicClass(Party):
    pass


class YogaClass(Party):
    pass
