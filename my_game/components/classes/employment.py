from ..images.images import GameGallery

gallery = GameGallery()


class Employment:
    def __init__(self, owner, image, position):
        self.owner = owner
        self.images = gallery.src_to_img(gallery.employment)
        self.image = self.images[self]
        self.position = position
        self.cash = 0
        self.inventory = 0
        self.expenses_and_income = {'bills and salaries': 0,
                                    'stuff cost': 0,
                                    'incomes': 0}

    def procurement(self):
        pass


class Butcher(Employment):
    pass


class Farmer(Employment):
    pass


class Dairy(Employment):
    pass


class Grocery(Employment):
    pass


class Greengrocer(Employment):
    pass


class Fisherman(Employment):
    pass


class Barber(Employment):
    pass


class Hunter(Employment):
    pass


class Tailor(Employment):
    pass


class Jeweler(Employment):
    pass


class Shepherd(Employment):  # contains chickens too
    pass


class Baker(Employment):
    pass


class WineryAndBrewery(Employment):
    pass


class University(Employment):
    pass


class Police(Employment):
    pass


class Court(Employment):
    pass


class DogShop(Employment):
    pass


class Textile(Employment):
    pass
