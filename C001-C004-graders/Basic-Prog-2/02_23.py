def is_palindrome(num):
    return str(num) == str(num)[::-1]

def nth_palindrome(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if is_palindrome(num):
            count += 1
    return num

n = int(input().strip())
result = nth_palindrome(n)
print(result)