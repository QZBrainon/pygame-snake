import pygame

class Settings():
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()

    def set_framerate(self,fps):
        self.clock.tick(fps)

    def ev():
        return pygame.event.get()


