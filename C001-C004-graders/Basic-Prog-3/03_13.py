input_list = [int(e) for e in input().split()]
k = int(input())

first_part = input_list[:k]
second_part = input_list[k:]

result = []

i, j = 0, 0
while i < len(first_part) and j < len(second_part):
    result.append(first_part[i])
    result.append(second_part[j])
    i += 1
    j += 1

while i < len(first_part):
    result.append(first_part[i])
    i += 1

while j < len(second_part):
    result.append(second_part[j])
    j += 1

print(result)