import random


a = 10
b = 20
print(a * b)
print(a / b)
print(a + b)
print(a - b)
print(a ** b)
print(a % b)
print(a // b)

if a >= 18:
    print("A,You are not eligible to vote")
else:
    print("You are not eligible to vote")
if b >= 18:
    print("B,You are not eligible to vote")
else:
    print("You are not eligible to vote")


a = [10, 20, 30, 40, 50]
b, c, d, e, f = a
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# global variable


z = 10


def func():
    global z
    z = 100
    print(z)


print(z)

func()
print(z)


list1 = ['ajay', 'kumar', 'chaturvedi']
print(random.choice(list1))

list = ['A', 'b', 'c']
print(random.shuffle(list), list)

if "a" in list:
    print("a is present")
else:
    print("a is not present")

if "ajay" in list1:
    print("ajay is present")
else:
    print("ajay is not present")

a = "Hello, woORld!"
print(a[2:5])

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
#a = "-------------Hello, woORld!------------------------------------"
# lstrip & strip to trim oout characters from the given string
print(a.rstrip('-'))
print(min(a))
print(max(a))


# occurence of character in string
print("")
print(a.index('w', 0, len(a)))
print(a.count('w', 0, len(a)))
print(a.find('w', 0, len(a)))

b = "my world ajay 🤣"

# print(a.join(b))

x = a.split(',')
print(x)

first = "data"
last = "scinece"
last_last = "toolbox"

print(first+last+last_last)
print(first+" "+last+" "+last_last)
