def frequency(number):
    frequency = {str(i): 0 for i in range(10)}
    for digit in number:
        frequency[digit] += 1
    result = ''.join(str(frequency[str(i)]) for i in range(10))
    print(result)

number = input().strip()
frequency(number)