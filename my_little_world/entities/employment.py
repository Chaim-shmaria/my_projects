from images.images import GameGallery

employment_images = GameGallery().employment


class Employment:
    def __init__(self, owner=None, position=None):  # need to delete default Nones
        self.owner = owner
        self.image = GameGallery().src_to_img(employment_images, f"{self}")
        self.position = position
        self.cash = 0
        self.inventory = 0
        self.expenses_and_income = {'bills and salaries': 0,
                                    'stuff cost': 0,
                                    'incomes': 0}

    def procurement(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}'


class Butchery(Employment):
    pass


class Farmer(Employment):
    pass


class Dairy(Employment):
    pass


class Grocery(Employment):
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

def employments_group():
    all_classes = [cls for cls in globals().values() if isinstance(cls, type)]

    # Exclude specific classes
    exclude_classes = [Employment, GameGallery]
    filtered_classes = [cls for cls in all_classes if cls not in exclude_classes]

    # Instantiate objects from each class
    return [cls() for cls in filtered_classes]

#print(employments_group())