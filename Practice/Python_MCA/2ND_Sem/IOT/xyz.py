# decimal to 4 bit binary
def binary(n):
    return bin(n).replace("0b", "")


def LED(n):
    pin = 25
    l = len(n)
    n = int(n)
    i = 0
    for i in range(0, l):
        rem = int(n / 10) * 10
        print(pin, rem)
        n /= 10
        pin -= 1


print(LED(binary(8)))
