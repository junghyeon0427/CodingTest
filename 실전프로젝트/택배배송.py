'''
BFS + BinSearch를 이용하는 문제
https://www.acmicpc.net/problem/1939
'''
from collections import deque


def bfs(weight):
    queue = deque()
    queue.append(A)
    visited = [False] * (N+1)
    visited[A] = True
    
    while queue:
        x= queue.popleft()

        for i, w in graph[x]:
            if not visited[i] and w >= weight:
                visited[i] = True
                queue.append(i)
                
    if visited[B]:
        return True
    else:
        return False

T = int(input())

for _ in range(T):
    N, M, A, B = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        O, D, C = map(int,input().split())
        graph[O].append([D, C])
        graph[D].append([O, C])
    
    start = 1
    end = 10000
    
    result = 0
    while start <= end:
        mid = (start + end) //2
    
        if bfs(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(result)
