def sierpinski_triangle(n):
    n+=1
    height = 2 ** n
    width = height
    triangle = [[" " for _ in range(width)] for _ in range(height)]

    for row in range(height):
        for col in range(width):
            if is_power_of_two(row, col):
                triangle[row][col] = "*"

    for row in triangle:
        print("".join(row).center(width))

def is_power_of_two(row, col):
    # Check if the row and col in the binary representation do not have a '1' in the same position
    # If they are, return False
    # If they are not, return True
    while row > 0 and col > 0:
        if row % 2 == 1 and col % 2 == 1:
            return False
        row //= 2
        col //= 2
    return True

n = int(input().strip())
sierpinski_triangle(n)