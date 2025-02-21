def process_list(lst):
    n = len(lst)
    chunk_size = n // 4

    chunks = []
    start = 0
    for i in range(4):
        end = start + chunk_size
        chunks.append(lst[start:end])
        start = end

    result = []
    
    result.extend(chunks[0][1::2])
    result.extend(chunks[1][::-1][2::3])
    result.extend(chunks[2][-3:])
    result.extend(chunks[3][::-1])
    
    return result

lst = [int(e) for e in input().split()]
result = process_list(lst)
print(result)