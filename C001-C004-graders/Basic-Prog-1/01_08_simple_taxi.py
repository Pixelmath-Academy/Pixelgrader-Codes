N = int(input())

fare = 35
if N <= 10:
    fare += N * 6
elif N <= 30:
    fare += 10 * 6 + (N - 10) * 7
else:
    fare += 10 * 6 + 20 * 7 + (N - 30) * 8

print(fare)