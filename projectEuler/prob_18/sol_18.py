# Project Euler #18: Maximum path sum I
# Find the maximum total from top to bottom of the triangle given in input.



def max_path_sum(triangle):
    for row in range(len(triangle)-1, 0, -1):
        for col in range(0, row):
            triangle[row-1][col] += max(triangle[row][col], triangle[row][col + 1])
    return(triangle[0][0])

t = int(input())



for _ in range(t):
    rows = int(input())
    triangle = []
    for r in range(rows):
        r = [int(i) for i in input().split(' ')]
        triangle.append(r)
    print(max_path_sum(triangle))
