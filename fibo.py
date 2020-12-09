" Different approach to fibo "

import time


def timerun(f):
    def wrap(*args):
        t1 = time.time()
        a = f(*args)
        t2 = time.time()
        print(f"runtime: {round(t2 - t1, 4)} sec")
        return a

    return wrap


@timerun
def fibo1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo1(n - 1) + fibo1(n - 2)


@timerun
def fibo2(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        memo[n] = fibo2(n - 1) + fibo2(n - 2)
        return memo[n]


@timerun
def fibo3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        counter = 1
        val = [0, 1]
        while counter < n:
            next_val = val[0] + val[1]
            val[0] = val[1]
            val[1] = next_val
            counter += 1
        return val[1]


print(fibo1(500))  # -> maximum recursion depth exceeded
print("-----------------")
print(fibo2(500))  # -> maximum recursion depth exceeded
print("-----------------")
print(fibo3(500))  # -> no problem :)
