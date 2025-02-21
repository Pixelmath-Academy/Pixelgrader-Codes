P = int(input())
R = int(input())
t = int(input())
n = int(input())

A = P * (1 + R / (100 * n)) ** (n * t)

print(round(A, 6))