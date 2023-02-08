# sum of elements in list
def sumOfListElements(n):

    size = len(n)
    max = 0
    sum = 0
    for i in range(0, size):
        sum += n[i]
        if max < n[i]:
            max = n[i]
    print(sum)
    print("Largest value is", max)


sumOfListElements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# common element in two lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 24, 3, 4, 55, 6, 37, 8, 29, 130]
c = []
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            c.append(a[i])
print(c)


# square of number 1 to 30 in list
a = []
for i in range(1, 31):
    a.append(i**2)


print(a[:6])
print(a[-5:])
