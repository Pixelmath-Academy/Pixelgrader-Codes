def nested_square(n):
    for i in range(n):
        for j in range(n):
            layer = min(i, j, n - 1 - i, n - 1 - j)
            print("*" if layer % 2 == 0 else "-", end="")
        print()

n = int(input().strip())
nested_square(n)
