n = int(input())
events = []
for _ in range(n):
    start, end = input().split()
    events.append((start, end))

max_events = 0

for minute in range(24 * 60):
    current_events = 0
    hour = minute // 60
    minute_of_hour = minute % 60
    current_time = (str(hour).zfill(2) + ":" + str(minute_of_hour).zfill(2))
    for start, end in events:
        if start <= current_time < end:
            current_events += 1
    if current_events > max_events:
        max_events = current_events

print(max_events)