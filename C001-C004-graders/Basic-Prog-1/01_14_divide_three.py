line1 = input().strip()
line2 = input().strip()
lst = line1.split()
lst.append(line2)
lst = lst[1:]
print(lst)