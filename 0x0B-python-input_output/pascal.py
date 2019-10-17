import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def pascal_triangle(n):
    pascal_list = []

    if n <= 0:
        return pascal_list

    for j in range(n):
        new_list = []
        for i in range(j + 1):
            new_list.append(int(nCr(j, i)))
        pascal_list.append(new_list)
    return pascal_list
