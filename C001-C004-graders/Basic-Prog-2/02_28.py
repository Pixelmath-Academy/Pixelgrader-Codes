def print_bar_graph():
    bars = []
    while True:
        num = int(input())
        if num <= 0:
            break
        bars.append(num)
    
    for num in bars:
        bar = ''
        for i in range(num):
            if (i + 1) % 5 == 0:
                bar += 'X'
            else:
                bar += '*'
        bar += str(num % 10)
        print(bar)

print_bar_graph()