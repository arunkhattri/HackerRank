# Day 3: Intro to conditional statements

# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird 
# If  is even and in the inclusive range of 2 to 5 ,print Not Weird 
# If  is even and in the inclusive range of 6 to 20,print Weird 
# If  is even and greater than 20 , print Not Weird 


def conditional_print(N):
    if N % 2 != 0:
        print('Weird')
    elif N % 2 == 0 and N in range(2,6):
        print('Not Weird')
    elif N % 2 == 0 and N in range(6, 21):
        print('Weird')
    else:
        print('Not Weird')

print(conditional_print(1))

######################################################################


def longest_subsequence(x):
    sorted_list = []
    for i in range(len(x)):
        if x[i] < x[i+1]:
            sorted_list.append(x[i])
            start = i
            break
    print('start: {}'.format(start))
    for i in range(start + 1, len(x)):
        if sorted_list[-1] < x[i]:
            sorted_list.append(x[i])
    return len(sorted_list)

x = [5, 2, 7, 4, 3, 8]
print(longest_subsequence(x))


def long_subseq(x):
    sorted_list = []
    for i in range(len(x)):
        if x[i] < x[i+1]:
            start = x[i]
            sorted_list.append(start)
            break
    y = x.index(start)
    print('y: {}'.format(y))
    for i in range(y + 1, len(x)):
        if sorted_list[-1] < x[i]:
            sorted_list.append(x[i])
    return len(sorted_list)

x = [5, 2, 7, 4, 3, 8]
print(long_subseq(x))




def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1                       # length of LIS found upto that moment
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        #  such that seq[M[j]] < seq[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]    # reversing

x = [3,2,6,4,5,1]
