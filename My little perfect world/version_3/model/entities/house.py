from model.images import GameGallery


house_images = GameGallery().house


class House:
    def __init__(self, pos):
        self.image = None
        self.position = pos
        self.Tenants = []
        self.content = []
        self.image = GameGallery().src_to_img(house_images, f"{self}")
