"""
A newly opened multinational brand has decided to base their company logo on the
three most common characters in the company name. They are now trying out
various combinations of company names and logos based on this condition. Given a
string 's' , which is the company name in lowercase letters, your task is to find
the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
'GOOGLE' would have it's logo with the letter G, O, E
"""
from collections import Counter


def three_most_common_char(string):
    c = Counter(sorted(string))
    for mc in c.most_common(3):
        print(f"{mc[0]} {mc[1]}")


if __name__ == "__main__":
    s = input()
    three_most_common_char(s)
