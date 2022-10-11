# try:
#     a = int(input("Enter a number: "))
#     if a == 0:
#         raise ("ZeroDivisionError")
#     b = int(input("Enter a number: "))
#     print(a/b)

# except ZeroDivisionError:
#     print("Enter non zero value as denominator")

# except ValueError:
#     print("Something wrong")

# except:
#     print("wrong")
# else:
#     print(a, b)


# a = '5'
# if not type(a) is int:
#     raise ("Enter integer value")

# print(a)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = a/b
# print(c)

class MyException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):

        return repr(self.value)


class code:
    c = 0

    def __init__(self):
        self.a = 10
        self.b = 4
        self.division(self)

    def division(self):
        self.c = self.a/self.b
        print(self.c)


c = code()
