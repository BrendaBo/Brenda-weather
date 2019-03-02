import math
class Point( ):
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def move1(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy
    def move2(self, step, angle=0):
        self.X = self.X + step * math.cos(angle)
        self.Y = self.Y + step * math.sin(angle)
    def __str__(self):
        return "point(%s,%s)"%(self.X, self.Y)
    def getX(self):
        return (self.X, self.Y)
    def getY(self):
        return self.Y
    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)
if __name__ == '__main__':
    a = Point(1,1)
    b = Point(3,3)
    print(a,b,a.distance(b))
    a.move1(4,3)
    print(a)

    

    

