class Sides:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


class Triangle(Sides):
    def __init__(self, *args):
        super(Triangle, self).__init__(*args)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5


a = int(input("Enter length of side1= "))
b = int(input("Enter length of side2= "))
c = int(input("Enter length of side3= "))
t = Triangle(a, b, c)
print(f"area : {t.area()}")