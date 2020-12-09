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


fibo1(500)  # -> maximum recursion depth exceeded
