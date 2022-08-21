"""
Given an interger, n, print the following values for each integer i from i to n:
1. Decimal
2. Octal
3. hexadecimal
4. Binary

Function Description:
---------------------
Complete the print_formatted function in the editor below:
print_formatted has the following parameters:
* int number: the maximum value to print

Prints
-----

The four values must be printed on a single line in the order specified above
for each i from 1 to number. Each value should be space-padded to match the width of the
binary value of number and the values should be separated by a single space.
"""


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec = i
        oct = f"{i:o}"
        hex = f"{i:X}"
        binary = f"{i:b}"

        print(f"{dec:>{width}} {oct:>{width}} {hex:>{width}} {binary:>{width}}")


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
