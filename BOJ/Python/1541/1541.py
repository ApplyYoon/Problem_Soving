import sys
input = sys.stdin.readline
string = input().strip()
splited = string.split('-')

for i, elem in enumerate(splited):
    group_sum = sum(int(num) for num in elem.split('+'))

    if i == 0:
        total = group_sum
    else:
        total -= group_sum

print(total)