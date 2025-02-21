mapping = {}
for i in range(26):
    letter = input().strip()
    mapping[chr(ord('a') + i)] = letter

encrypted_message = input().strip()

decoded_message = ''.join(mapping[char] for char in encrypted_message)

print(decoded_message)