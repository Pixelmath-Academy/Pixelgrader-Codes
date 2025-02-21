n, k = (int(e) for e in input().split())
cookies = n // k
coupons = cookies
trays = cookies

while coupons >= 2 or trays >= 4:
    free_cookies = (coupons // 2) + (trays // 4)
    cookies += free_cookies
    coupons = (coupons % 2) + free_cookies
    trays = (trays % 4) + free_cookies

print(cookies)