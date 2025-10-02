import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    applicants = []

    for _ in range(N):
        doc, interview = map(int, input().split())
        applicants.append((doc, interview))

    applicants.sort(key=lambda x: x[0])

    count = 1
    min_interview = applicants[0][1]

    for i in range(1, N):
        if applicants[i][1] < min_interview:
            count += 1
            min_interview = applicants[i][1]

    print(count)