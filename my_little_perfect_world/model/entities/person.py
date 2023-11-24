from model.images import GameGallery


person_images = GameGallery().person


class Person:
    def __init__(self, gender, age, employment, children):
        self.age = age
        self.gender = gender
        self.image = None
        self.employment = employment
        self.children = children
        self.cash = None
        self.satisfaction = None
        self.happiness = None
        self.needs = {'food': 4,
                      'employment': 8,
                      'sex': 5,
                      'happiness': 5}
        self.image = GameGallery().src_to_img(person_images, f"{self}")
