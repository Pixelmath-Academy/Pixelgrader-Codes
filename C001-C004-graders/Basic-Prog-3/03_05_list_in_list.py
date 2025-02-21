lst = []
current_list = lst

while True:
    command = input().strip()
    if command.startswith('a '):
        _, x = command.split()
        current_list.append(int(x))
    elif command == 'l':
        new_list = []
        current_list.append(new_list)
        current_list = new_list
    elif command == 's':
        print(lst)
        break