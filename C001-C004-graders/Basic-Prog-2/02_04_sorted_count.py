n = int(input())
strings = input().split()

count_dict = {}
for e in strings:
    if e in count_dict:
        count_dict[e] += 1
    else:
        count_dict[e] = 1

for key in sorted(count_dict):
    print(key + ": " + str(count_dict[key]))