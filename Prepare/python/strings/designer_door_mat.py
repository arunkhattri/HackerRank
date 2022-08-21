"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a
new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs
--------------
    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""


def designer_door_mat(length, width):
    core = ".|."
    filler = "-"
    text = "WELCOME"
    mid = (width // 2) + 1

    for i in range(1, mid):
        print((core * ((2 * i) - 1)).center(length, filler))
    print(text.center(length, filler))
    for i in range(mid - 1, 0, -1):
        print((core * ((2 * i) - 1)).center(length, filler))


if __name__ == "__main__":
    length, width = input().split(" ")
    designer_door_mat(int(width), int(length))
