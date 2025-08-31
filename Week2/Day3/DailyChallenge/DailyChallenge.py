import math
class Circle:
    def __init__(self, *, radius= None, diameter = None):
       
        if radius and diameter and radius*2 != diameter:
            raise ValueError ("You have provided 2 non-coherent parameters.Please provide EITHER radius OR diameter.")
        self.radius = radius or diameter / 2
        self.diameter = diameter or radius * 2
        self.area = math.pi * (self.radius ** 2)

    def __str__(self)->str:
        return f"Radius : {self.radius}, Area : {self.area:.2f}"

    def __add__(self,other):
        new_radius = self.radius + other.radius
        return Circle(radius = new_radius)
    
    def __eq__(self,other):
        return self.area == other.area
    
    def __ge__(self,other):
        return self.area >= other.area
    
    def __lt__(self,other):
        return self.area < other.area
   
c1 = Circle(radius=2)
c2 = Circle(diameter=3)
try:
    c5 = Circle(radius=2, diameter=3)
except:
    pass
print(c1)
print(c2)
print(c1+c2)
print(c1==c2)
print(c1>=c2)

# Put circles in the list and sort them
circles = [Circle(radius=3),Circle(radius=5), Circle(radius=1)]
circles.sort()
for c in circles:
    print(c)

