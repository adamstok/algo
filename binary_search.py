def search(arr,el):
    l = 0
    r = len(arr) - 1
    count = 0
    while True:
        m = (l+r) // 2
        if l > r :
            print(f'{el} not found !')
            return False
        elif arr[m] < el:
            count += 1
            l = m + 1
            print(count, f' : {arr[m]} < {el}')
        elif arr[m] > el:
            count += 1
            r = m - 1
            print(count, f' : {arr[m]} > {el}')
        elif arr[m] == el:
            print(f'{el} found on index {m}')
            return m

