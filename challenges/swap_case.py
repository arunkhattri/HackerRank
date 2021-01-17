# Problem: given a string, swap cases. convert all lowercases letters to uppercase letters and vice versa.


def swap_cases(s):
    """Swap cases"""
    res = []
    for elem in s:
        if isinstance(elem, str) and elem.islower():
            res.append(elem.upper())
        elif isinstance(elem, str) and elem.isupper():
            res.append(elem.lower())
        else:
            res.append(elem)
    return "".join(res)


if __name__ == "__main__":
    case1 = "Pythonist 2"
    print(swap_cases(case1))
