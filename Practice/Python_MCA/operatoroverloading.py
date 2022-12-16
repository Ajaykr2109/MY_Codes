# calculating the distance of two points using operator overloading

from pickle import FALSE, TRUE
from re import A


class cord:
    def set(self, x, y):
        self.__x = x
        self.y = y

    def distance(self, ob2):
        d = ((self.__x-ob2.__x))**2+((self.y-ob2.y)**2)**0.5
        return d

    def __sub__(self, i2):
        return self.distance(i2)


p1 = cord()
p2 = cord()

p1.set(7, 4)
p2.set(12, 5)

# a1 = p1.distance(p2)
# print(a1)

print("Distance between two points is ", p2-p1)


# checking whether thecircles are same with their ccircumferences or not

class circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        a = 3.14*self.radius**2
        return a

    def __eq__(p1, p2):
        if p1.radius == p2.radius:
            return TRUE
        else:
            return FALSE


ob1 = circle(10)
ob2 = circle(1)

a1 = ob1.area()
a2 = ob2.area()

print(ob1 == ob2)
print(a1)
print(a2)
