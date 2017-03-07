# Project Euler #22: Names Scores
# Given Q queries, each query is a name, print the score


def names_score(names, name):
    nl = names
    nl_sorted = sorted(nl)
    alpha_score = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    final_score = []
    for nm in name:
        name_pos = nl_sorted.index(nm)
        name_sc = 0
        for i in list(nm):
            name_sc += alpha_score.index(i) + 1
        fs = name_sc * (name_pos + 1)
        final_score.append(fs)
    return(final_score)


n = int(input())
names = []
for _ in range(n):
    nm = input()
    names.append(nm)
q = int(input())
name = []
for _ in range(q):
    nm = input()
    name.append(nm)

scores = names_score(names, name)
for sc in scores:
    print(sc)
