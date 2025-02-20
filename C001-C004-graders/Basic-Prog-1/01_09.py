a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Not a triangle")
else:
    if a == 60 and b == 60 and c == 60:
        print("Equilateral")
    else:
        is_right = a == 90 or b == 90 or c == 90
        is_isosceles = a == b or b == c or a == c
        is_scalene = a != b and b != c and a != c
        
        if is_right and is_isosceles:
            print("Right\nIsosceles")
        elif is_right:
            print("Right")
        elif is_isosceles:
            print("Isosceles")
        elif is_scalene:
            print("Scalene")