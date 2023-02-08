def frequentElement(n):
    maxCount = 0
    index = -1
    for i in range(len(n)):
        count = 0
        for j in range(len(n)):
            if n[i] == n[j]:
                count += 1
        if count > maxCount:
            maxCount = count
            index = i
    if maxCount > 1:
        print(n[index])
    else:
        print("No element is repeated")


# remove even numbers from list and print
def removeEven(list):
    i = 0
    # print(len(n))
    list1 = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list1.append(list[i])
    for ele in list1:
        list.remove(ele)
    print(list)


# Python program to convert a list of characters into a string.
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    print(str1)


# find equilibrium index of list
def equilibriamIndex(n):
    for i in range(len(n)):
        leftSum = 0
        rightSum = 0
        for j in range(i):
            leftSum += n[j]
        for k in range(i + 1, len(n)):
            rightSum += n[k]
        if leftSum == rightSum:
            print(i)
            return
    print("No such index exists")
    return


frequentElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10])
removeEven([2, 3, 4, 5, 6, 7, 8, 9, 88, 44, 22])
listToString(
    [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
)
equilibriamIndex([1, 2, 3, 6, 3, 3])
