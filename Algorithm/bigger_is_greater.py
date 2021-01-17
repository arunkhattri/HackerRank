word = 'hcdk'
w = list(word)
w.reverse()
print(w)


def longest_non_increasing(w):
    """
    find longest non increasing suffix in a given word
    Parameters
    ----------
    w: string, contains letters in the range ascii[a..z]
    Returns
    -------
    string, longest non increasing suffix
    string, pivot
    """
    elem = ""
    pivot = ""
    for i in range(len(w)-1):
        if w[i] > w[i+1]:
            elem += w[i]
        elif w[i] < w[i+1] and w[i] < w[i-1]:
            elem +=w[i]
            pivot = w[i+1]
    return elem, pivot


def next_permutation(w):
    """
    XXX
    """
    arr = list(w)
    # find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0 :
        return 'no answer'
    # longest suffix is arr[i:]

    # find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i-1]

    # reverse suffix
    arr[i:] = arr[len(arr)-1: i-1:-1]
    return "".join(arr)

