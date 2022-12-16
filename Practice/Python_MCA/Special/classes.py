# # calling base class constructor from derived class object

# class animal:
#     def speak(self):
#        # super(d).speak()
#         print("Mai jaanwar hu!!!")


# class dog(animal):
#     def speak(self):
#         print("Mai bhokta hu!")
#         super().speak()


# d = dog()
# # a = animal()
# d.speak()
# animal.speak()
# animal.speak(d)

# function and operator overloading in class lpu


class lpu:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print("Addition operator overloaded")
        return self.a + other.a, self.b + other.b

    def __eq__(self, other):
        print("Equality operator overloaded")
        return self.a == other.a, self.b == other.b

    def __str__(self):
        return 'a = {}, b = {}'.format(self.a, self.b)


def main():
    lpu1 = lpu(10, 20)
    lpu2 = lpu(30, 40)
    print(lpu1 + lpu2)
    print(lpu1 == lpu2)
    print(lpu1)
    print(lpu2)


main()
