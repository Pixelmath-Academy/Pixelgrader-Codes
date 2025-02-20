def print_square_pattern(n):
    
    print('*' * n)
    
    for _ in range(n - 2):
        print('*' + ' ' * (n - 2) + '*')
    
    print('*' * n)

n = int(input().strip())
print_square_pattern(n)