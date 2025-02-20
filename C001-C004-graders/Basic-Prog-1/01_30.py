lst = [int(e) for e in input().split()]

n = len(lst)

for i in range(n):
    lst = lst[1:] + lst[:1]
    print(lst)
    