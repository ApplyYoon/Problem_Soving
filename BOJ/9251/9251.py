import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()


width = max(len(str1), len(str2))
table = [[0 for col in range(width)] for row in range(width)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:                 
            if i-1 == -1 or j-1 == -1:
                table[i][j] = 1
            else:
                table[i][j] = table[i-1][j-1] + 1

        else:
            
            if i-1 == -1 and j-1 != -1:
                table[i][j] = table[i][j-1]

            elif i-1 != -1 and j-1 == -1:
                table[i][j] = table[i-1][j]

            elif i-1 == -1 and j-1 == -1:
                table[i][j] = 0

            else:
                table[i][j] += max(table[i-1][j], table[i][j-1])

print(max(max(table)))