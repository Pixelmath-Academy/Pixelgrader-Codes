def print_vertical_graph(numbers):
    max_value = max(numbers)
    for level in range(max_value + 1, 0, -1):
        line = ""
        for num in numbers:
            if num + 1 == level:
                line += str(num % 10) + " "
            elif num >= level:
                if level % 5 == 0:
                    line += "# "
                else:
                    line += "* "
            else:
                line += "  "
        print(line.rstrip())

numbers = [int(e) for e in input().split()]
print_vertical_graph(numbers)