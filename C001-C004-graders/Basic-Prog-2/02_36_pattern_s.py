current_char = ord('A')

def next_char():
    global current_char
    char = chr(current_char)
    current_char += 1
    if current_char > ord('Z'):
        current_char = ord('A')
    return char

def s_pattern(n):
    print(" ".join(next_char() for _ in range(n))[::-1])

    for i in range(1, n - 1):
        print(next_char())

    print(" ".join(next_char() for _ in range(n)))

    for i in range(n - 2):
        print(" " * (2 * (n - 1)) + next_char())

    print(" ".join(next_char() for _ in range(n))[::-1])

n = int(input().strip())
s_pattern(n)