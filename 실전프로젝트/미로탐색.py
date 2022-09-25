'''
BFS를 이용해서 인덱스마다 시작점에서부터의 거리를 기록
'''

from collections import deque

t = int(input())

for _ in range(t):
    N, M = map(int, input().split(' '))
    arr = [[] for _ in range(N)]
    
    for i in range(N):
        tmp = input()
        for j in tmp:
            arr[i].append(int(j))
            
    cnt = 0
    deq = deque([[0, 0, cnt]])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    arr[0][0] = '1'
    
    while deq:
        ix, iy, cnt = deq.popleft()
        for i in range(4):
            new_x = ix + dx[i]
            new_y = iy + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if arr[new_x][new_y] == 1:
                    arr[new_x][new_y] += int(arr[ix][iy]) 
                    deq.append([new_x, new_y, cnt+1])
    arr[0][0] = 1
                    
    print(arr[N-1][M-1])
