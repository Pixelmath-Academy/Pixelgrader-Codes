numbers = [int(e) for e in input().split()]

ascending = numbers[:]
ascending.sort()

descending = numbers[:]
descending.sort(reverse=True)

print(ascending)
print(descending)