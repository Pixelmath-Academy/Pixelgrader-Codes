def find_largest_root(N, R):
    i = 0
    while True:
        power = i ** R
        equation = " x ".join([str(i)] * R)
        if power < N:
            print("Step " + str(i + 1) + ": " + equation + " = " + str(power) + " (less than " + str(N) + ")")
        elif power == N:
            print("Step " + str(i + 1) + ": " + equation + " = " + str(power) + " (equal to " + str(N) + ")")
            print("Answer is " + str(i))
            return
        else:
            print("Step " + str(i + 1) + ": " + equation + " = " + str(power) + " (more than " + str(N) + ")")
            print("Answer is " + str(i - 1))
            return
        i += 1

n, r = [int(e) for e in input().split()]
find_largest_root(n, r)