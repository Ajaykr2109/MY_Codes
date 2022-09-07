
def fib(n):
    t,t1=0,1
    for i in range (1,n):
        sum=t+t1
        #print(sum)
        t=t1
        t1=sum
    return sum

print(fib(eval(input())))