normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = int(input())
k = a
for i in range(a):
    for j in range(k):
        print(normal[j], end="")
    k -= 1
    print()
