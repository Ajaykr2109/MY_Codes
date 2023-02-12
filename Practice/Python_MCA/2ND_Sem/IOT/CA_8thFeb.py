# 1.palindrome numbers from 1 to 200
# 2.difference between two list


def palindrome(n):
    for i in range(10, n + 1):
        temp = i
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp = temp // 10
        if i == rev:
            print(i, " ", end="")


print(palindrome(200))


def differenceTwoList(List1, list2):
    return list(set(List1) - set(list2))


print(differenceTwoList([1, 2, 3, 4, 5], [1, 2, 3]))
