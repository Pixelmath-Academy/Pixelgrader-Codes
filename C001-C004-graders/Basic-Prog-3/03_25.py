def find_largest_root(N):
    i = 0
    while i * i <= N:
        if i * i < N:
            print("Step " + str(i + 1) + ": " + str(i) + " x " + str(i) + " = " + str(i * i) + " (less than " + str(N) + ")")
        elif i * i == N:
            print("Step " + str(i + 1) + ": " + str(i) + " x " + str(i) + " = " + str(i * i) + " (equal to " + str(N) + ")")
        i += 1
    if (i - 1) * (i - 1) < N:
        print("Step " + str(i + 1) + ": " + str(i) + " x " + str(i) + " = " + str(i * i) + " (more than " + str(N) + ")")
    if i - 1 == -1:
        print("Answer is 0")
    else:
        print("Answer is " + str(i - 1))


N = int(input())
find_largest_root(N)