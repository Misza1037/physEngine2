#object.py


from vector import Vector as v
import pygame

class screenObject:
    def __init__(self, size, pointer):
        #IMPLEMENTED:
        # Screen Size
        # Screen Object from pyGame
        if type(size) not in [tuple, list]: raise TypeError('screenObject.__init__.size')
        if len(size) != 2: raise ValueError('screenObject.__init__.size')
        if not (type(size[0]) == int and type(size[1]) == int): raise TypeError('screenObject.__init__.size')
        self.screenSize = size
        if type(pointer) != pygame.Surface: raise TypeError('screenObject.__init__.pointer')
        self.screen = pointer

class BASEpyGameConfigClass:
    def __init__(self, screen, framerate):
        #IMPLEMENTED:
        # screenObject
        if type(screen) != screenObject: raise TypeError('BASEpyGameConfigClass.__init__().screen')
        self.screen = screen
        if type(framerate) != int: raise TypeError('')
        if framerate <= 0: raise ValueError('')
        self.framerate = framerate

class BASEphysicsConfigClass:
    def __init__(self, gravitationalAcceleration=v(0,10), bounceCoefficient=1.0):
        #IMPLEMENTED:
        # g Acceleration
        # bounce Coeff
        if type(gravitationalAcceleration) not in [v]: raise TypeError('BASEphysicsConfigClass.__init__().gravitationalAcceleration')
        self.gravitationalAcceleration = gravitationalAcceleration # <acceleration vector>
        if type(bounceCoefficient) not in [int, float]: raise TypeError('BASEphysicsConfigClass.__init__().bounceCoefficient')
        if bounceCoefficient > 1: raise ValueError('BASEphysicsConfigClass.__init__().bounceCoefficient')
        if bounceCoefficient < 0: raise ValueError('BASEphysicsConfigClass.__init__().bounceCoefficient')
        self.bounceCoefficient = bounceCoefficient # <float, int>:=<0,1>


class base:
    def __init__(self, pyGame, phys):
        #IMPLEMENTED:
        # pyGame Config
        # physics Config
        # list of objects
        if type(pyGame) != BASEpyGameConfigClass:  raise TypeError( 'base.__init__().pyGame' )
        if type(phys)   != BASEphysicsConfigClass: raise TypeError( 'base.__init__().phys'   )
        self.pyGame = pyGame
        self.phys = phys




        self.obj = {}
    def addObj(self, ID, object):
        if ID in self.obj: raise ValueError( 'base.addObj().ID' )
        self.obj[ID] = object
    def removeObj(self, ID):
        if ID not in self.obj: raise ValueError( 'base.removeObj(),ID' )
        self.obj.pop(ID)
    def cycle(self):
        self.pyGame.screen.screen.fill((255, 255, 255))
        for ID, object in self.obj.items():
            object.computePhysics()
            object.draw()
            object.endCycle()
            pygame.display.flip()

class OBJpyGamePropertiesClass:
    def __init__(self):
        pass
class OBJphysicsPropertiesClass:
    def __init__(self, mass):
        #IMPLEMENTED:
        # mass
        if type(mass) not in [int, float]: raise TypeError('')
        if mass < 0: raise ValueError('')
        self.mass = mass
        self.externalForces = {'1':v(0,0)}
        self.temporaryForces = [v(0,0)]
class Object:
    def __init__(self, _base, xy, pyGame, phys, r):
        #IMPLEMENTED:
        # BASE
        # x, y coordinates
        # pyGame properties
        # phys properties
        if type(_base) != base: raise TypeError('')
        self.base = _base
        if type(xy) != list: raise TypeError('')
        if len(xy) != 2: raise ValueError('')
        if type(xy[0]) not in [int, float] or type(xy[1]) not in [int, float]: raise TypeError('')
        self.color = (0, 0, 0)
        self.r = r
        self.x = xy[0]
        self.y = xy[1]
        if type(pyGame) != OBJpyGamePropertiesClass: raise TypeError('')
        self.pyGame = pyGame
        if type(phys) != OBJphysicsPropertiesClass: raise TypeError('')
        self.phys = phys
        self.v0 = v(0,0)
    def acceleration(self):
        externalForcesSum = v(0,0)
        for i in self.phys.externalForces:
            externalForcesSum += self.phys.externalForces[i]
        temporaryForcesSum = v(0,0)
        for i in self.phys.temporaryForces:
            temporaryForcesSum += i
        return (externalForcesSum+temporaryForcesSum).mulBy(1/self.phys.mass) + self.base.phys.gravitationalAcceleration
    def velocity(self):
        return (
            self.v0 + self.acceleration()
        ).mulBy(1/self.base.pyGame.framerate)
    def computePhysics(self):
        velocity = self.velocity()
        self.x += velocity.x/self.base.pyGame.framerate
        self.y += velocity.y/self.base.pyGame.framerate
    def draw(self):
        pygame.draw.circle(self.base.pyGame.screen.screen, self.color, self.pos(), self.r)
    def endCycle(self):
        pass
    def pos(self):
        return (int(self.x), int(self.y))
