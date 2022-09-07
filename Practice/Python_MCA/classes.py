from ast import Try


class animal:
    def speak(self):
        print("Hello, I am Kutta!!")


class dog(animal):
    super().speak()
    def speak(self):
        print("Hello, mai gunga hu!!")


d = dog()
d.speak()


