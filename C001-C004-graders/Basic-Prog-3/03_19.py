def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    prev_char = s[0]
    
    for i in range(1, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            if count > 2:
                result.append(prev_char + str(count))
            else:
                result.append(prev_char * count)
            prev_char = s[i]
            count = 1
    
    if count > 2:
        result.append(prev_char + str(count))
    else:
        result.append(prev_char * count)
    
    return ''.join(result)

input_string = input().strip()
compressed_string = compress_string(input_string)
print(compressed_string)