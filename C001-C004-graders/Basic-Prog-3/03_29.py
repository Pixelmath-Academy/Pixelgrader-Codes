def is_half_hearted(message):
    count_A = message.count('A')
    count_B = message.count('B')
    count_C = message.count('C')
    
    if count_A == count_B == count_C:
        return True
    
    n = len(message)
    i = 0
    while i < n:
        j = i
        while j < n and message[j] == message[i]:
            j += 1
        new_message = message[:i] + message[j:]
        new_count_A = new_message.count('A')
        new_count_B = new_message.count('B')
        new_count_C = new_message.count('C')
        if new_count_A == new_count_B == new_count_C:
            return True
        i = j
    
    return False

message = input()
if is_half_hearted(message):
    print("YES")
else:
    print("NO")