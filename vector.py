#vector.py


#class:Vector
class Vector:

    #__init__:<vector>, <int/float>, <int/float>
    def __init__(self, x, y):

        if type(x) not in [int, float]: raise TypeError( 'Vector.__init__().x' )
        self.x = x
        if type(y) not in [int, float]: raise TypeError( 'Vector.__init__().y' )
        self.y = y

    #__add__:<vector>, <vector>
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    #__neg__:<vector>
    def __neg__(self):
        return Vector(-self.x, -self.y)

    #__sub__:<vector>, <vector>
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    #__str__:<vector>
    def __str__(self):
        return f'<{self.x},{self.y}>'

    #__repr__->__str__:<vector>
    def __repr__(sefl):
        return '<vector>'

    #mulBY:<vector>, <int/float>
    def mulBy(self, value):
        if type(value) not in [int, float]: raise TypeError('')
        return self.vector(self.x*value, self.y*value)
