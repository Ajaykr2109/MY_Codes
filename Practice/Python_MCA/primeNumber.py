import time

st=time.process_time()
def isprime(n):
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
def main():
    for i in range(1,10000):
        if isprime(i):
            print(i)
main()

et=time.process_time()
print(et-st)


