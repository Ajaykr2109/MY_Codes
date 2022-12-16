import time
from timeit import timeit

st = time.process_time()

memo = {}


def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(500, memo))
print(memo)

et = time.process_time()
# check time taken by the above code
print(et - st)
