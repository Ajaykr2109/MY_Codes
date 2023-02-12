# # remove duplicates
# class Solution:
#     def removeDuplicates(self, input1):

#         if input1 is None or len(input1) == 0:
#             return ""
#         # check input is string or not
#         if not isinstance(input1, str):
#             return None

#         ans = ""
#         for i in input1:
#             if i not in ans:
#                 ans += i
#         return ans


# print(Solution().removeDuplicates("aabbccdd"))

# # python 3.6
# # remove duplicates
# class solution:
#     def removeduplicates(self, input1):
#         # return "".join(set(input1))
#         return "".join(dict.fromkeys(input1))


# print(solution().removeduplicates("aabbccdd"))

# def leapYear(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False

# import re

# import re
# text= input()
# compil = re.compile('(?<=('+input()+'))') # (?<=...) is a positive lookbehind assertion
# if compil.search(text) is not None:
#     for i in compil.finditer(text):
#        print((i.start(1),i.end(1)-1))
# else:
#     print((-1, -1))

#    def getPossibleGridCoordinates(x, y, z, n):
#     print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]) #  list comprehension

# #what is list comprehension
# # list comprehension is a way to create a list in a single line of code
# # how list comprehension works
# # list comprehension is a way to create a list in a single line of code
# # we can use list comprehension to create a list of squares of first 5 numbers
# # syntax [expression for item in list]
# # example [i*i for i in range(5)]
# # example [i*i for i in range(5) if i%2 == 0]
# # example [i*i for i in range(5) if i%2 == 0 if i%3 == 0]
# # example [i*i for i in range(5) if i%2 == 0 if i%3 == 0 else i+1]
# # example [i*i for i in range(5) if i%2 == 0 if i%3 == 0 else i+1 for j in range(5)]
# # example [i*i for i in range(5) if i%2 == 0 if i%3 == 0 else i+1 for j in range(5) if j%2 == 0 if j%3 == 0 else j+1]
# # example [i*i for i in range(5) if i%2 == 0 if i%3 == 0 else i+1 for j in range(5) if j%2 == 0 if j%3 == 0 else j+1 if j%4 == 0]

# n = int(5)
# arr = map(int, "1 2 3 6 6 4 5".split())
# # map to list
# if n >= 2 and n <= 10:
#     lst = list(arr)
#     for i in lst:
#         if i >= -100 and i <= 100:
#             continue
#         else:
#             print("Error")
#     lst = list(set(lst))
#     lst.sort()
# print(lst[-2])

dict = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
score = []

# for _ in range(0, 3):
#     name = input()
#     for j in range(0, 3):
#         score = float(input())
#     dict[name] = score
# recent = input()

# if recent in dict:
#     avg = (dict[recent][0] + dict[recent][1] + dict[recent][2]) / 3
#     # show two decimal places

#     print(avg)
# add key value pair in list comprehension
# dict = {i: i * i for i in range(1, 11)}
# print(dict)
# accesing dictionary which has list as value
# dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# print(dict['a'][0])

# accesing dictionary which has list as value all at once
# for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line als
# print(i * (10**i - 1) // 9) # how this works?
# class EvenStream(object):
#     def __init__(self):
#         self.current = 0

#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return

# class OddStream(object):
#     def __init__(self):
#         self.current = 1

#     def get_next(self):
#         to_return = self.current
#         self.current += 2
#         return to_return

# def print_from_stream(n, stream=None):
#     if stream is None:
#         stream = EvenStream()
#     for _ in range(n):
#         print(stream.get_next())


# queries = int(input())
# for _ in range(queries):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())


def fun(s):
    # return True if s is a valid email, else return False
    import re

    if re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s):
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
