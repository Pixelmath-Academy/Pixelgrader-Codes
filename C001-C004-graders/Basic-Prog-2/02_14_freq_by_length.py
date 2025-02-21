n = int(input())
words = [input().strip() for _ in range(n)]

length_dict = {}
for word in words:
    length = len(word)
    if length not in length_dict:
        length_dict[length] = []
    length_dict[length].append(word)

result = []
for length in sorted(length_dict.keys()):
    words_with_length = sorted(length_dict[length])
    result.append([length, words_with_length, len(words_with_length)])

print(result)