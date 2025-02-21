n = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
length = len(alphabet)

for i in range(n):
    row = ''
    for j in range(n):
        row += alphabet[(i * n + j) % length] + ' '
    print(row.strip())