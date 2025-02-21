n, r = [int(e) for e in input().split()]

for i in range(1, n + 1):
    if i == 1 or i == n:
        print('-' * r + '*' * (n - 2 * r) + '-' * r)
    elif 1 < i <= r:
        print('-' * (r - i + 1) + '*' + '*' * (n - 2 * r + 2 * (i - 2)) + '*' + '-' * (r - i + 1))
    elif r < i <= r + n - 2 * r:
        print('*' + '*' * (n - 2) + '*')
    elif r + n - 2 * r < i < n:
        print('-' * (r - n + i) + '*' + '*' * (n - 2 * r + 2 * (n - i - 2) + 2) + '*' + '-' * (r - n + i))
