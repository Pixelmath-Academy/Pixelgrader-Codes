n, x, y = (int(e) for e in input().split())

def spiral_value(n, x, y):
    l = min(x, y, n - 1 - x, n - 1 - y)
    s = n - l * 2
    if s == 1:
        return n * n
    total_numbers = 0
    for k in range(l):
        s_k = n - k * 2
        if s_k == 1:
            num_elements = 1
        else:
            num_elements = (s_k * 4) - 4
        total_numbers += num_elements
    start_num = total_numbers + 1
    x_min, y_min = l, l
    x_max, y_max = n - l - 1, n - l - 1
    if y == y_min:
        offset = x - x_min
    elif x == x_max:
        offset = (s - 1) + (y - y_min)
    elif y == y_max:
        offset = (s - 1) * 2 + (x_max - x)
    else:
        offset = (s - 1) * 3 + (y_max - y)
    return start_num + offset

print(spiral_value(n, x, y))