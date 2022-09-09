#calling base class constructor from derived class object

class animal:
    def speak(self):
       # super(d).speak()
        print("Mai jaanwara hu!!!")


class dog(animal):
    def speak(self):
       print("Mai bhokta hu!")
       super().speak()


d = dog()
a = animal()
d.speak()
animal.speak() 
animal.speak(d) 

 
