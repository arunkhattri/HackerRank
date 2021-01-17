# task: You are given a string. Split the string on a " " (space) delimiter
# and join using a - hyphen.


def split_and_join(line):
    """Split the string and join by hyphen"""
    return line.replace(" ", "-")


if __name__ == "__main__":
    SOME_STR = "this is a string"
    print(split_and_join(SOME_STR))
