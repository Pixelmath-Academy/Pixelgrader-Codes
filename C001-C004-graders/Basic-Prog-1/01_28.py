int_list = [int(e) for e in input().split()]
position, new_value = (int(e) for e in input().split())
int_list[position] = new_value
print(int_list)