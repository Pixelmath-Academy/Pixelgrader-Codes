def is_perfect_number(n):
    if n < 2:
        return "NO"
    
    sum_divisors = 1
    
    for i in range(2, n):
        if n % i == 0:
            sum_divisors += i
    
    if sum_divisors == n:
        return "YES"
    else:
        return "NO"

n = int(input())
print(is_perfect_number(n))