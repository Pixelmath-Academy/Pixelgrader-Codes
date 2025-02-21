n = int(input())
sets = [set(int(e) for e in input().split()) for _ in range(n)]
intersection_set = sets[0]
for s in sets[1:]:
    intersection_set &= s
print(len(intersection_set))