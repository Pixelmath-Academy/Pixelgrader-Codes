A = set(int(e) for e in input().split())
B = set(int(e) for e in input().split())

result = sorted(A ^ B)

print(result)