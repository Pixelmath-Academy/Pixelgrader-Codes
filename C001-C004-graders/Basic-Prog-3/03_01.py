def grade_student(n):
    n = int(n)
    prime_numbers = {2, 3, 5, 7}
    
    if 110 <= n < 120 and n % 2 == 0:
        print("A+++")
    elif 75 <= n <= 85 and n % 5 == 0:
        print("A$#")
    elif 1 <= n <= 10 and n in prime_numbers:
        print("B")
    elif 55 <= n <= 60:
        print("C++")
    elif 30 <= n <= 80 and n % 3 == 0:
        print("D^")
    elif 30 <= n <= 80 and n % 5 == 0 and n % 3 != 0:
        print("Z--")
    elif 90 <= n <= 100 and n % 2 != 0:
        print("F++")
        print("Congrats on failing!")
    elif n == 100:
        print("G#")
    elif 20 <= n <= 90 and (n % 10 == 1 or n % 10 == 3):
        print("Q@")
    elif 33 <= n <= 77 and n % 11 == 0:
        print("J/")
    elif n == 120:
        print("O_O")
    else:
        print("F---")

n = input()
grade_student(n)