import pygame

EMPLOYMENT_PREFIX = '..//images//source//employment//'

class GameGallery:
    def __init__(self):
        self.employment = {
            'Butchery':          f'{EMPLOYMENT_PREFIX}Butchery.jpg',
            'Farmer':            f'{EMPLOYMENT_PREFIX}Farmer.jpg',
            'Dairy':             f'{EMPLOYMENT_PREFIX}Dairy.jpg',
            'Grocery':           f'{EMPLOYMENT_PREFIX}Grocery.jpg',
            'Fisherman':         f'{EMPLOYMENT_PREFIX}Fisherman.jpg',
            'Barber':            f'{EMPLOYMENT_PREFIX}Barber.jpg',
            'Hunter':            f'{EMPLOYMENT_PREFIX}Hunter.png',
            'Tailor':            f'{EMPLOYMENT_PREFIX}Tailor.jpg',
            'Jeweler':           f'{EMPLOYMENT_PREFIX}Jeweler.jpg',
            'Shepherd':          f'{EMPLOYMENT_PREFIX}Shepherd.jpg',
            'Baker':             f'{EMPLOYMENT_PREFIX}Baker.jpg',
            'WineryAndBrewery':  f'{EMPLOYMENT_PREFIX}WineryAndBrewery.jpeg',
            'University':        f'{EMPLOYMENT_PREFIX}University.jpg',
            'Police':            f'{EMPLOYMENT_PREFIX}Police.jpg',
            'Court':             f'{EMPLOYMENT_PREFIX}Court.jpeg',
            'DogShop':           f'{EMPLOYMENT_PREFIX}DogShop.jpg',
            'Textile':           f'{EMPLOYMENT_PREFIX}Textile.jpeg'

        }
        self.house = {}
        self.party = {}
        self.person = {}
        self.recreation = {}
        self.ground = {}

    # def src_to_img(self, src_dict):
    # loaded = {}
    # for subject in src_dict.keys():
    #     src = src_dict[subject]
    #     loaded[subject] = pygame.image.load(src)
    # return loaded

    def src_to_img(self, src_dict, subject):
        src = src_dict[subject]
        loaded = pygame.image.load(src)
        return loaded
