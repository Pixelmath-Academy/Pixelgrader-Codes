import math

mu, sigma, x = [float(e) for e in input().split()]
f_x = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
print('%.6f' % f_x)