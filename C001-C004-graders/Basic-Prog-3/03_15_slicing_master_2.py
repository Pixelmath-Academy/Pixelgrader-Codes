lst = [int(e) for e in input().split()]
even_lst = [lst[i] for i in range(len(lst)) if i % 2 == 1]
k = len(lst) % 4

if k > 0:
    indices_to_remove = list(range(0, len(even_lst), k + 1))
    even_lst = [even_lst[i] for i in range(len(even_lst)) if i not in indices_to_remove]

for i in range(len(even_lst)):
    if i % 2 == 0:
        even_lst[i] = even_lst[i] ** 2

print(even_lst)