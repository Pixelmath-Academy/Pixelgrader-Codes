def count_ordered_pairs(z):
    count = 0
    for x in range(1, z + 1):
        for y in range(1, z + 1):
            if x**2 + y**2 == z**2:
                count += 1
    print(count)

z = int(input())
count_ordered_pairs(z)