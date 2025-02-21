def gcd_euclidean(x, y):
    step = 1
    while y != 0:
        remainder = x % y
        print("Step", step, ": a =", x, ", b =", y, ", remainder =", remainder)
        x, y = y, remainder
        step += 1
    print("GCD is", x)

x, y = (int(e) for e in input().split())
gcd_euclidean(x, y)