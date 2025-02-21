heights = [int(e) for e in input().split()]
max_height = max(heights)
positions = []
result = []
current_pos = 0
for h in heights:
    width = 2 * h - 1
    center = current_pos + width // 2
    positions.append((center, h))
    current_pos += width + 1
total_width = current_pos - 1
for level in range(max_height, 0, -1):
    line = [' '] * total_width
    for center, h in positions:
        if h >= level:
            offset = h - level
            start = center - offset
            end = center + offset
            if level == h:
                line[center] = '#'
            else:
                for i in range(start, end + 1):
                    line[i] = '*'
    print(''.join(line).rstrip())