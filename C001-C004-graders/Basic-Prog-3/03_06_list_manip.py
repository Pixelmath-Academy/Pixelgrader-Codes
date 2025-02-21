def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_list(lst):
    total_sum = sum(lst)
    even_count = sum(1 for x in lst if x % 2 == 0)
    odd_count = len(lst) - even_count

    results = []

    if total_sum % 3 == 0:
        results.append(lst[::-1])
    if even_count % 2 == 0 and odd_count % 2 != 0:
        results.append(sorted(lst))
    if lst[-1] > lst[0]:
        results.append(sorted(set(lst), reverse=True))
    if is_prime(total_sum):
        results.append([x**2 for x in lst])
    
    if results:
        for result in results:
            print(result)
    else:
        print("ngong pai mod la")

input_list = [int(e) for e in input().split()]
process_list(input_list)