def cool_diamond(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        if i == 1:
            print(spaces + '#')
        else:
            print(spaces + '#' + '*' * (2 * i - 3) + '#')
    
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        if i == 1:
            print(spaces + '#')
        else:
            print(spaces + '#' + '*' * (2 * i - 3) + '#')

n = int(input().strip())
cool_diamond(n)