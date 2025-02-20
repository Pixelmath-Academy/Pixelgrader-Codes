s = input().strip()
even_count = 0
odd_count = 0

for char in s:
    digit = int(char)
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, odd_count)