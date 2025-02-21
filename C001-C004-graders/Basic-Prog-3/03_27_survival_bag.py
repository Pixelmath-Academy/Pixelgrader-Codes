def max_survival_days(x, y, z):
    day = 0
    while True:
        day += 1
        if day % 2 == 1:
            x -= 2
            y -= 1
        else:
            x -= 1
            y -= 2
        
        if day % 3 == 0:
            z -= 1
        if day % 5 == 0:
            z -= 1
        
        if x < 0 or y < 0 or z < 0:
            return day + 3 - 1

x, y, z = (int(e) for e in input().split())
print(max_survival_days(x, y, z))