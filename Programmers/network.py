def solution(n, computers):
    answer = 0
    visit = [0] * n  # 각 컴퓨터의 방문 여부 체크

    def dfs(node):
        visit[node] = 1  # 현재 노드 방문 처리
        for neighbor in range(n):
            # 연결되어 있고(1), 아직 방문하지 않은 노드라면 이동
            if computers[node][neighbor] == 1 and visit[neighbor] == 0:
                dfs(neighbor)

    for i in range(n):
        if visit[i] == 0:  # 아직 어느 네트워크에도 속하지 않은 노드 발견
            dfs(i)         # 해당 노드와 연결된 모든 노드를 방문 처리
            answer += 1    # 새로운 네트워크 발견으로 간주
            
    return answer
