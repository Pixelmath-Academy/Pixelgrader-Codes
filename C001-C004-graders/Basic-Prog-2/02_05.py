def check_duplicates(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return "YES"
        char_count[char] = 1
    return "NO"

input_string = input().strip()
print(check_duplicates(input_string))