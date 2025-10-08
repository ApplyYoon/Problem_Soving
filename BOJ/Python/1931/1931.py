import sys
input = sys.stdin.readline

n = int(input().strip())
items = []
for _ in range(n):
    start, end = input().strip().split()
    start, end = int(start), int(end)
    items.append((start, end))

items.sort(key=lambda x: (x[1], x[0]))  
last_end = 0
count = 0
for start, end in items:
    if start >= last_end:
        count += 1
        last_end = end

print(count)