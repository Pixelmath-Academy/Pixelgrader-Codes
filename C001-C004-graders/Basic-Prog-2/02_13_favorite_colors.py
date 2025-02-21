n = int(input())
color_dict = {}

for i in range(1, n + 1):
    colors = input().split()
    for color in colors:
        if color in color_dict:
            color_dict[color].append(i)
        else:
            color_dict[color] = [i]

result = sorted([(color, sorted(people)) for color, people in color_dict.items()])
print(result)