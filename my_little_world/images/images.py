import pygame


class GameGallery:
    def __init__(self):
        self.employment = {
            'Butchery': '..//images//source//employment//Butchery.jpg',
            'Farmer': '..//images//source//employment//Farmer.jpg',
            'Dairy': '..//images//source//employment//Dairy.jpg',
            'Grocery': '..//images//source//employment//Grocery.jpg',
            'Fisherman': '..//images//source//employment//Fisherman.jpg',
            'Barber': '..//images//source//employment//Barber.jpg',
            'Hunter': '..//images//source//employment//Hunter.png',
            'Tailor': '..//images//source//employment//Tailor.jpg',
            'Jeweler': '..//images//source//employment//Jeweler.jpg',
            'Shepherd': '..//images//source//employment//Shepherd.jpg',
            'Baker': '..//images//source//employment//Baker.jpg',
            'WineryAndBrewery': '..//images//source//employment//WineryAndBrewery.jpeg',
            'University': '..//images//source//employment//University.jpg',
            'Police': '..//images//source//employment//Police.jpg',
            'Court': '..//images//source//employment//Court.jpeg',
            'DogShop': '..//images//source//employment//DogShop.jpg',
            'Textile': '..//images//source//employment//Textile.jpeg'

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
