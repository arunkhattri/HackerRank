# https://www.hackerrank.com/challenges/grading/problem
# grade: 0 to 100
# less than 40: fail
# diff between the grade and the next multiple of 5 is less than 3
# round grade up to the next multiple of 5.
# no rounding of grade below 40


def next_multiple(n):
    if n % 5 == 0:
        return n
    else:
        return n - (n % 5) + 5


def final_grade(original_grade):
    if original_grade < 38:
        return original_grade
    elif next_multiple(original_grade) - original_grade < 3:
        return next_multiple(original_grade)
    else:
        return original_grade


if __name__ == "__main__":
    N = [73, 67, 38, 33]
    for n in N:
        print(f"[-] Original Grade: {n} --> Final Grade: {final_grade(n)}")
        
    
