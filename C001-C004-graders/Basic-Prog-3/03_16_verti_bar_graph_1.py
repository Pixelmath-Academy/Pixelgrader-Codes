input_line = input()
numbers = [int(e) for e in input_line.split()]
max_height = max(numbers)
for level in range(max_height, 0, -1):
    line = ''
    for number in numbers:
        if number >= level:
            line += '* '
        else:
            line += '  '
    print(line.rstrip())