import pygame
import os
import random

PIPE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))]


class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = 0
        self.GAP = 100
        self.VELOCITY = 5
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, xbool=False, ybool=True)
        self.PIPE_BOTTOM = PIPE_IMAGE

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VELOCITY

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)  # returns None if not colliding
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point or t_point:
            return True

        return False
