# #call one constructor from another constructor in one class

# from typing import overload
# from overload import overloads
# from dispatcher import dispatcher
# from timed import timed

# dispatcher is a class that is used to dispatch the method calls to the appropriate method of the class based on the type of the object that is passed as an argument. The dispatching is done by the type of the object that is passed as an argument.
# an object is being created at the back end and all the abstract operations are being added in to that object with add((int(data type), func name)) method.
# dispatcher utilises decorator to add the abstract operations to the object.
# decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

import time
from multipledispatch import dispatch
from timeit import timeit


st = time.process_time()


class animal:

    @dispatch()  # overloaded #overloads
    def __init__(self):
        print("constructor 1")
        self.__init__(2, 2)

    @dispatch(int, int)  # @Overload
    def __init__(self, i, j):
        print("constructor 2")
        #i *= j
        #self.__init__(2, 2, 2)
       # print(i)

    @dispatch(int, int, int)
    def __init__(self, j, k, l):
        print("Constructor 3")
        x = j**k**l
        print(x)


a = animal(10, 10)

et = time.process_time()
print(et-st)
