def concatinate(lst):
    n1=[]
    for i in lst:
        if i[0] == i[1]:
            n1.append(i)
        else:
            n1.append(i[0])
            n1.append(i[1])
        return n1
n1=[(3, 4), (3, 5), (3, 9), (6, 11), (6, 8, 7)]      
print(concatinate(n1))

