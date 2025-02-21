def moo_deng(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=', ' if j < i else '')
        for j in range(i - 1, 0, -1):
            print(', ' if j == i - 1 else '', end='')
            print(j, end=', ' if j > 1 else '')
        print()

n = int(input())
moo_deng(n)