max_value = int(input())

while True:
    value = int(input())
    if value == -1:
        break
    if value > max_value:
        max_value = value

print(max_value)