from statistics import mean, median, mode


l1 = list("hello")
l2 = list(range(5, 50+1, 5))
# print(l1)
print(l2)

if 'e' in l1:
    print("True")
if 'e' not in l2:
    print("True")
l3 = l1+l2
l1.append(l2)
# print(l3)
# print(l1)
# print(l1[5][10])

print(l2[:])

# slice(list name, first element index,final index+1)
# if we put negative index python will automatically add the length of the list to the index
