import pygame


class GameGallery:
    def __init__(self):
        self.employment = {}
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
