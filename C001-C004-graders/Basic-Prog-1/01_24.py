n, k = [int(e) for e in input().split()]
c = n // k
p = c

while p >= 2:
    free_cookies = p // 2
    c += free_cookies
    p = p % 2 + free_cookies

print(c)