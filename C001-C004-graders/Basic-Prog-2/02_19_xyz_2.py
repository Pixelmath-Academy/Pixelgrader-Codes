import math

def count_perfect_squares(n):
    count = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                if is_perfect_square(x + y**2 + z**3):
                    count += 1
    return count

def is_perfect_square(num):
    root = int(math.sqrt(num))
    return root * root == num

n = int(input())
print(count_perfect_squares(n))