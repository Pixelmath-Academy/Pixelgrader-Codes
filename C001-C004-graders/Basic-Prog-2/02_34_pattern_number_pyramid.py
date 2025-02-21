def number_pyramid(n):
    current_num = 0
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        
        for j in range(2 * i + 1):
            print(current_num, end='')
            current_num = (current_num + 1) % 10
        
        print()

n = int(input().strip())
number_pyramid(n)