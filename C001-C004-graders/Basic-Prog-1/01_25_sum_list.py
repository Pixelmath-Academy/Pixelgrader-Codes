list1 = [int(e) for e in input().split()]
list2 = [int(e) for e in input().split()]

if len(list1) != len(list2):
    print("ERROR")
else:
    result = [list1[i] + list2[i] for i in range(len(list1))]
    print(result)