from ..images.images import GameGallery

gallery = GameGallery()


class Person:
    def __init__(self, gender, age, employment, children):
        self.age = age
        self.gender = gender
        self.image = None
        self.employment = employment
        self.childern = children
        self.cash = None
        self.satisfaction = None
        self.happiness = None
        self.needs = {'food': 4,
                      'employment': 8,
                      'sex': 5,
                      'happiness': 5}
        self.images = gallery.src_to_img(gallery.person)
        self.image = self.images[self]
