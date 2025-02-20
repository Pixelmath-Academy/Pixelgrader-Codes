import math

def reduce_fraction(x, y):
    gcd = math.gcd(x, y)
    reduced_x = x // gcd
    reduced_y = y // gcd
    
    if reduced_y == 1:
        return str(reduced_x)
    else:
        return str(reduced_x) + '/' + str(reduced_y)

x, y = (int(e) for e in input().split())
print(reduce_fraction(x, y))