# Globals for the bearings
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)


class Robot(object):
    x = 0
    y = 0
    coordinates = (0, 0)
    bearing = NORTH
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        coordinatestemp = (self.x, self.y)
        self.coordinates = coordinatestemp
        self.bearing = bearing
        
    def turn_left(self):
        if self.bearing == EAST:
            self.bearing =  NORTH
        elif self.bearing == NORTH:
            self.bearing =  WEST
        elif self.bearing == WEST:
            self.bearing =  SOUTH
        else:
            self.bearing =  EAST
            
    def turn_right(self):
        if self.bearing == EAST:
            self.bearing =  SOUTH
        elif self.bearing == NORTH:
            self.bearing =  EAST
        elif self.bearing == WEST:
            self.bearing =  NORTH
        else:
            self.bearing =  WEST
            
    def advance(self):
        self.x += self.bearing[0]
        self.y += self.bearing[1]
        coordinatestemp = (self.x, self.y)
        self.coordinates = coordinatestemp
        
    def simulate(self, strsimulate):
        for x in strsimulate:
            if x == "L":
                self.turn_left()
            elif x == "R":
                self.turn_right()
            else:
                self.advance()
