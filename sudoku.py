# chaque ligne, colonne et région ne doit contenir qu'une seule fois tous les chiffres de un à neuf
import os
from random import randint


def ShowGrid(g):
    for y in range(9):
        if y % 3 == 0 and y != 0:
            print("-" * (8 * 9 - 7))
            print((" " * 20 + "|   ") * 2)
        for x in range(9):
            if (x + 1) % 3 == 0 and x != 8:
                print(str(g[y][x]) + "   |   ", end="")
            else:
                print(str(g[y][x]) + "\t", end="")
        print()
        print((" " * 20 + "|   ") * 2)


def is_in_horizontal(g, y, n):
    # print("horizontal", g[y], n, n in g[y])
    return n in g[y]


def is_in_vertical(g, x, n):
    # print("vertical", [y[x] for y in g], n, n in [y[x] for y in g])
    return n in [y[x] for y in g]


def is_in_box(g, y, x, n):
    """9 box :
    (0,0), (0,3), (0,6),
    (3,0), (3,3), (3,6),
    (6,0), (6,3), (6,6)"""
    if y in [0, 1, 2]:
        y = 0
    elif y in [3, 4, 5]:
        y = 3
    else:
        y = 6
    if x in [0, 1, 2]:
        x = 0
    elif x in [3, 4, 5]:
        x = 3
    else:
        x = 6
    # print("box", (y, x))
    for Y in range(3):
        for X in range(3):
            if n == g[y + Y][x + X]:
                return True
    return False


def possible_place(g, y):
    existing_n = []  # liste des nombres qui sont déja sur la ligne (number)
    for x in range(9):
        if g[y][x] != 0:
            existing_n.append(g[y][x])
    l = []  # liste des nombres qui ne sont pas déja sur la ligne (number)
    for x in range(1, 10):
        if not x in existing_n:
            l.append(x)

    all_p = []
    for i in range(len(l)):
        n = l[i]
        p = []
        for x in range(9):
            if (
                is_in_horizontal(g, y, n)
                + is_in_vertical(g, x, n)
                + is_in_box(g, y, x, n)
                + g[y][x]
                != 0
            ) == 0:
                p.append(x)
        all_p.append((n, p, len(p)))  # (number, [x1, x6, x2...], nbs possi in y)
    return all_p, l


def get_min_random(all_p, l):
    l = [i for i in range(len(l))]
    min_n = (0, 0, 10)
    while len(l) != 0:
        i = randint(0, len(l) - 1)
        if all_p[l[i]][-1] < min_n[-1]:
            min_n = (
                all_p[l[i]][0],
                all_p[l[i]][1][randint(0, len(all_p[l[i]][1]) - 1)]
                if len(all_p[l[i]][1]) > 1
                else all_p[l[i]][1][0],
                all_p[l[i]][-1],
            )
        del l[i]
    return min_n


def init_grid():
    g = []
    row = [0] * 9
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(9):
        index = randint(0, len(l) - 1)
        row[x] = l[index]
        l.__delitem__(index)
    g.append(row)
    for y in range(8):
        g.append([0] * 9)
    return g


def init_grid_V2():
    g = [0] * 9
    for y in range(9):
        g[y] = [0] * 9
    return g


def add_row(g, y):
    for _ in range(9):
        # input()
        # ShowGrid(g)
        p, l = possible_place(g, y)
        # print("possible places :")
        # for r in p:
        #     print("-", r)
        if impossible(p):
            return False
        n = get_min_random(p, l)
        g[y][n[1]] = n[0]
    return g


def impossible(p):
    for k in range(len(p)):
        for i in range(k + 1, len(p)):
            if len(p[k][1]) == 1 and len(p[i][1]) == 1:
                if p[k][1] == p[i][1]:
                    return True
    return False


def add_row_v2(g, y):
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(9):
        i = randint(0, len(l) - 1)
        n = l[i]
        while (
            is_in_horizontal(g, y, n)
            or is_in_vertical(g, x, n)
            or is_in_box(g, y, x, n)
        ):
            i = randint(0, len(l) - 1)
            n = l[i]

        g[y][x] = n
        # ShowGrid(g)
    return g


def add_box(g, y, x):
    l_n = [i + 1 for i in range(9)]
    for Y in range(3):
        for X in range(3):
            rdn = randint(0, len(l_n) - 1)
            n = l_n[rdn]
            while is_in_horizontal(g, y + Y, n) or is_in_vertical(g, x + X, n):
                rdn = randint(0, len(l_n) - 1)
                n = l_n[rdn]
                print(n, l_n)
                ShowGrid(g)
                input()

            g[y + Y][x + X] = l_n[rdn]
            del l_n[rdn]
    return g


def add_number(g, n):
    l_index = [i for i in range(9)]
    for y in range(9):
        rdn = randint(0, len(l_index) - 1)
        while g[y][l_index[rdn]] != 0 or is_in_box(g, y, l_index[rdn], n):
            rdn = randint(0, len(l_index) - 1)
        g[y][l_index[rdn]] = n
        del l_index[rdn]


not_succes = 0
total = 1000
for i in range(total):
    g = init_grid()
    for y in range(1, 9):
        g = add_row(g, y)
        if g == False:
            not_succes += 1
            break
    # os.system("cls")
    # print("_" * 10 + str(i + 1) + "/" + str(total) + "_" * 10)
print(
    str(total - not_succes) + "/" + str(total),
    str(round((total - not_succes) / total * 100, 2)) + "% succed",
)
