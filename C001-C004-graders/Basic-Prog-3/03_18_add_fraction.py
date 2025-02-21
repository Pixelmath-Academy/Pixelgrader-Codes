def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b, c, d = (int(e) for e in input().split())

num = a * d + c * b
den = b * d

g = gcd(num, den)
num //= g
den //= g

rat_num = num / den

print(str(num) + "/" + str(den) + " " + str(round(rat_num, 6)))