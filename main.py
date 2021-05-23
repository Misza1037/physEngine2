#main.py
from time import time
start = time()
from vector import Vector as v
import pygame
from object import BASEpyGameConfigClass
from object import BASEphysicsConfigClass
from object import base
from object import screenObject
from object import Object
from object import OBJpyGamePropertiesClass
from object import OBJphysicsPropertiesClass
from functions import check_events
from pygame.time import Clock
pygame.init()
screenSize = [500, 500]
screen = pygame.display.set_mode(screenSize)
SCREEN = screenObject(screenSize, screen)
_basePyGame  = BASEpyGameConfigClass(SCREEN)
_basePhysics = BASEphysicsConfigClass()
BASE = base(_basePyGame, _basePhysics)





BASE.addObj('ball', Object(BASE, [100,100], OBJpyGamePropertiesClass(), OBJphysicsPropertiesClass(1)))






end = time()
print(f'loading time: {end - start}s')


def run():
    # FPS settings
    FPS_max = 60.0
    FPS_delta = 0.0
    FPS_clock = Clock()

    # Game loop
    while True:

        FPS_delta += FPS_clock.tick() / 1000.0
        if FPS_delta > 1 / FPS_max:
            check_events(SCREEN.screen, BASE)
            BASE.cycle()

            FPS_delta -= 1 / FPS_max

#####

run()

pygame.quit()
