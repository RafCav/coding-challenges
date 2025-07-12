"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set(s[1] for s in students))  # set → unique grades, then sort
    second_lowest = grades[1]  # Unique second lowest grade

    names = sorted([s[0] for s in students if s[1] == second_lowest])  # Names mathing second lowest grade

    for n in names:  # name are in a list
        print(n)  # printing each one



