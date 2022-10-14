

class B1:
    def __init__(self, t):
        self.s = t  # instance variable and it can be inherited
       # print("B1 constructor", self.s)

    def display(self):
        print("B1 display", self.s)


class B2:
    def __init__(self, t):
        self.s = t
      #  print("B2 constructor", self.s)

    def display(self):
        print("B2 display", self.s)


class D(B1, B2):
    def __init__(self, t, t1, t2):
        super().__init__(t)
        super(B1, self).__init__(self, t1)
        self.d = t2
        B1.display(self)
        B2.display(self)
        print("D constructor", self.d)

    def display(self):
        print("D display", self.s)


d = D(10, 20, 30)
