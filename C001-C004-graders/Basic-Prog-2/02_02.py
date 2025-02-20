n, m = [int(e) for e in input().split()]
name_dict = {}

for _ in range(n):
    first_name, last_name = input().split()
    name_dict[first_name] = last_name

for _ in range(m):
    query = input().strip()
    if query in name_dict:
        print(name_dict[query].strip())
    else:
        print("kor tod sang kom")