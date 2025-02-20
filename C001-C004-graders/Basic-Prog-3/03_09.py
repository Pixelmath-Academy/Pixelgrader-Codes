import math

def simplify_square_root(n):
    largest_square = 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % (i * i) == 0:
            largest_square = i * i
    outside_sqrt = int(math.sqrt(largest_square))
    inside_sqrt = n // largest_square
    if outside_sqrt == 1:
        print('sqrt', inside_sqrt)
    elif inside_sqrt == 1:
        print(outside_sqrt)
    else:
        print(outside_sqrt, 'sqrt', inside_sqrt)

n = int(input())
simplify_square_root(n)