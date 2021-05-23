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
pygame.init()
screenSize = [500, 500]
screen = pygame.display.set_mode(screenSize)
SCREEN = screenObject(screenSize, screen)
_basePyGame  = BASEpyGameConfigClass(SCREEN)
_basePhysics = BASEphysicsConfigClass()
BASE = base(_basePyGame, _basePhysics)



BASE.addObj('ball', Object(BASE, [100,100], OBJpyGamePropertiesClass(), OBJphysicsPropertiesClass(1)))
for ID, object in BASE.obj.items():
    object.computePhysics()
    object.draw()
end = time()
print(f'loading time: {end - start}s')

#####




#####

pygame.quit()
