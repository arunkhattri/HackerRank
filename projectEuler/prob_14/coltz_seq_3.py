# Collatz Sequence


from array import array


def efficient_loop(n):
    arr = array('i', [0] * 100)
    arr[0] = 1
    for i in range(2, n+1):
        num = i
        count = 0
        # print("***************************************************")
        # print("i = {}; num = {}; count = {}".format(i, num, count))
        condition = True
        while condition:
            if num % 2 == 0:
                num = num // 2
                count += 1
                # print("if: num= {}; count= {}".format(num, count))
            elif num % 2 != 0:
                num = (3 * num + 1) // 2
                count += 2
                # print("else: num= {}; count= {}".format(num, count))
            if num < len(arr) and arr[num - 1] != 0:  # array starts from 0
                condition = False
            # print("num = {} ; arr[num] = {}".format(num, arr[num-1]))
        if num != 1:
            arr[i-1] = count + arr[num - 1]
        else:
            arr[i-1] = count
    return arr


def result(n):
    res = array('i', [])
    arr = efficient_loop(n)
    seq = arr[0]
    pos = 1
    res.append(pos)
    for i in range(2, n+1):
        new_seq = arr[i-1]
        if new_seq >= seq:
            pos = i
            seq = new_seq
            res.append(pos)
        else:
            res.append(pos)
    return res
