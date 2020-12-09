" Different approach to fibo "

import time


def timerun(f):
    def wrap(*args):
        t1 = time.time()
        a = f()
        t2 = time.time()
        print(f"runtime: {round(t2 - t1, 4)}")
        return a

    return wrap
