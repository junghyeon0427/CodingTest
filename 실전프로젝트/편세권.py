'''
matrix의 모든 지점에서 마다 편의점간의 거리를 통해 점수를 저장
작은 인덱스부터 '>' 일때만 저장하기 때문에 같을 때 처리 해줄 필요가 없다.
'''

t = int(input())

for _ in range(t):
    n, c = map(int, input().split(' '))
    convi = list()
    cnt = 0
    matrix = [[0] * n for _ in range(n)]
    
    for _ in range(c):
        x, y = map(int, input().split(' '))
        matrix[x][y] = -1
        convi.append([x, y])
        
    max_cnt = [0, 0, 0]
    
    for i in range(n):
        for j in range(n):
            # 편의점이 있는 곳 -> 점수 계산 x
            if matrix[i][j] == -1:
                continue
            # 편의점 마다 거리 계산을 통해 점수 계산
            for x, y in convi:
                tmp_dist = abs(x - i) + abs(y - j)
                if tmp_dist <= 3:
                    cnt += 3
                elif tmp_dist <= 10:
                    cnt += 1
            if cnt > max_cnt[2]:
                max_cnt = [i, j, cnt]
            cnt = 0
            
    for i in max_cnt:
        print(i, end=' ')
    print()
