def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

s = input().strip()
char_count = count_characters(s)

max_count = max(char_count.values())
print(max_count)