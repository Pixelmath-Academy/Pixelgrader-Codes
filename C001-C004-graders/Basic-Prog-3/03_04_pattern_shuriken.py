m = int(input())
for i in range(m):
    print(" " * (m - i + m - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*", end="")
        print("-" * (2 * i - 1), end="")
        print("*")

for i in range(m // 2):
    print(" " * (2 * (m - i) - m - 2), end="")
    print("*", end="")
    print("-" * (m + i), end="")
    if i == 0:
        print("#", end="")
    else:
        print("#", end="")
        print(" " * (2 * i - 1), end="")
        print("#", end="")
    print("-" * (m + i), end="")
    print("*")

for i in range(m // 2 - 2, -1, -1):
    print(" " * (2 * (m - i) - m - 2), end="")
    print("*", end="")
    print("-" * (m + i), end="")
    if i == 0:
        print("#", end="")
    else:
        print("#", end="")
        print(" " * (2 * i - 1), end="")
        print("#", end="")
    print("-" * (m + i), end="")
    print("*")

for i in range(m - 1, -1, -1):
    print(" " * (m - i + m - 1), end="")
    if i == 0:
        print("*")
    else:
        print("*", end="")
        print("-" * (2 * i - 1), end="")
        print("*")