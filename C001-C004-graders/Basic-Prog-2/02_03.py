n, m = [int(e) for e in input().split()]
students = {}

for _ in range(n):
    student_id, room_number = [int(e) for e in input().split()]
    if room_number not in students:
        students[room_number] = []
    students[room_number].append(student_id)

for _ in range(m):
    room_number = int(input())
    if room_number in students:
        print(sorted(students[room_number]))
    else:
        print([])