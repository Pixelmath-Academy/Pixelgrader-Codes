def process_input(input_string):
    numbers = [int(e) for e in input_string.split()]
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers)
    print(sorted_numbers)

input_string = input()
process_input(input_string)