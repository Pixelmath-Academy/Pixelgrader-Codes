C = int(input())

if C < 0:
    print("It's freezing!")
elif 0 <= C <= 15:
    print("It's chilly!")
elif 16 <= C <= 30:
    print("It's nice!")
else:
    print("It's hot!")