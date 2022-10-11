
import time
from timeit import timeit

st = time.process_time()


def fib(n):
    t, t1, sum = 0, 1, 0
    for i in range(1, n):
        sum = t+t1
        # print(sum)
        t = t1
        t1 = sum
    return sum


def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)


def sum(n):
    sum = 0
    if n == 1:
        return 1
    else:
        return n+sum(n-1)


a = eval(input("Enter the number: "))
if (a == 1):
    print("Fibonacci series is: ")
    print(fib(a))
else:
    print("Fibonacci series is: ")
    for i in range(1, a+1):
        print(fib(i))
print("")

et = time.process_time()
# check time taken by the above code
print(et-st)
