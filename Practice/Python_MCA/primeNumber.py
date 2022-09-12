import time

st = time.process_time()


def isprime(n):
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True


def main(n):
    c = 0
    if (n <= 664580):
        for i in range(1, 10000000):
            if isprime(i):
                c = c+1
                x = i
                if (c == n):
                    break
        print("Index is", c, end=" ")
        print("Number is", x)
    else:
        print("Invalid")


i = int(input("Enter Index for the adjacent Prime Number: "))
main(i)

et = time.process_time()
print(et-st)
