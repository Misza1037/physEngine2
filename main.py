#main.py
from time import time
start = time()
from vector import Vector as v
import pygame
from object import BASEpyGameConfigClass
from object import BASEphysicsConfigClass
from object import base
from object import screenObject

pygame.init()
screenSize = [500, 500]
screen = pygame.display.set_mode(screenSize)
SCREEN = screenObject(screenSize, screen)
_basePyGame  = BASEpyGameConfigClass(SCREEN)
_basePhysics = BASEphysicsConfigClass()
BASE = base(_basePyGame, _basePhysics)
end = time()
print(f'loading time: {end - start}s')
pygame.quit()
