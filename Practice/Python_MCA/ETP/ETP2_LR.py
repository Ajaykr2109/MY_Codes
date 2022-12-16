# sum of prime numbers between 1 to 100 ending with 7


# def prime(n):
#     sum = 0
#     for i in range(1, n + 1):
#         if i % 10 == 7:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 sum += i
#     return sum


# print(prime(100))

# create a matrix values 1-100  with * in left and right diagonal
# def star(n):
#
#     for i in range(n):
#         for j in range(n):
#             if i == j or j == n - 1 - i:
#                 print("*", end=" ")
#                 n += 1
#             else:
#
#                 print(n, end="  ")
#         print()


def star(n):
    a = 1
    for i in range(n):
        for j in range(n):
            if i == j or j == n - 1 - i:
                print("*", end=" ")
                a += 1
            else:
                a += 1
                print(a, end="  ")
        print()


star(10)
