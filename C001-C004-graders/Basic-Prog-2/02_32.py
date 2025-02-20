def striped_pyramid(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print('*' * i)
        else:
            print('#' * i)

n = int(input().strip())
striped_pyramid(n)