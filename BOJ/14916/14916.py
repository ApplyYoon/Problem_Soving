import sys
input = sys.stdin.readline
N = int(input().strip())
answer = 10**6

# 2로만 나눌 수 있다면 후보에 추가
if N%2 == 0:
    answer = N//2

# 13일 경우, 5가 들어갈 수 있는 경우의 수는 2번(1번 넣거나, 2번 넣거나)
# 1번 넣은 경우 남은 값은 8 <-- 이 값을 2로 나눌 수 있다면 후보에 추가
for i in range(1, (N//5)+1):
    result = 0

    temp = N - (5*i)
    result += i

    if temp%2==0:
        result += (temp//2)
        if answer > result:
            answer = result

# 만약 한 번도 발견하지 못했다면 오답처리
if answer == 10**6:
    answer = -1

print(answer)