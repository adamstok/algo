import time


def runtime(f):
    def wrap(*args):
        t1 = time.time()
        outp = f(*args)
        t2 = time.time()
        print(f"runtime : {t2-t1} sec")
        return outp

    return wrap


@runtime
def search(arr, el):
    l = 0
    r = len(arr) - 1
    count = 0
    while True:
        m = (l + r) // 2
        if l > r:
            print(f"{el} not found !")
            return False
        elif arr[m] < el:
            count += 1
            l = m + 1
            print(count, f" : {arr[m]} < {el}")
        elif arr[m] > el:
            count += 1
            r = m - 1
            print(count, f" : {arr[m]} > {el}")
        elif arr[m] == el:
            print(f"{el} found on index {m}")
            return m


sortedarr = [
    2,
    3,
    8,
    45,
    67,
    123,
    345,
    452,
    652,
    788,
    876,
    4566,
    76899,
    88665,
    5464545645,
]
search(sortedarr, 876)


# In a sorted array they could be duplicates. Below is the function to get te most left (duplicated or not ) element.


@runtime
def search_left(arr, el):
    l = 0
    r = len(arr)
    count = 0
    while l < r:
        m = (l + r) // 2
        if arr[m] < el:
            count += 1
            print(f"{count}: {arr[m]} < {el}")
            l = m + 1
        else:
            count += 1
            print(f"{count}: {arr[m]} >= {el}")
            r = m
    if arr[l] == el:
        print(f"{el} found on index {l}")
        return l
    elif l > r:
        print(f"{el} not found !")
        return False


sorted_dups = [
    2,
    2,
    2,
    3,
    8,
    8,
    45,
    67,
    123,
    123,
    123,
    345,
    452,
    652,
    788,
    788,
    788,
    876,
    4566,
    76899,
    88665,
    5464545645,
]
search_left(sorted_dups, 2)
search_left(sorted_dups, 8)
search_left(sorted_dups, 788)


# In a sorted array they could be duplicates. Below is the function to get te last searched element (duplicated or not ) element.
@runtime
def search_right(arr, el):
    l = 0
    r = len(arr)
    count = 0
    while l < r:
        m = (l + r) // 2
        if arr[m] > el:
            count += 1
            print(f"{count}: {arr[m]} > {el}")
            r = m
        else:
            count += 1
            print(f"{count}: {arr[m]} <= {el}")
            l = m + 1
    if arr[r - 1] == el:
        print(f"{el} found on index {r-1}")
        return r - 1
    elif l > r:
        print(f"{el} not found !")


sorted_dups = [
    2,
    2,
    2,
    3,
    8,
    8,
    45,
    67,
    123,
    123,
    123,
    345,
    452,
    652,
    788,
    788,
    788,
    876,
    4566,
    76899,
    88665,
    5464545645,
]
search_right(sorted_dups, 2)
search_right(sorted_dups, 8)
search_right(sorted_dups, 788)
