'''
물음표가 나오는 열까지 사타리 타기 진행
-> 물음표가 나오는 지점에서 왼쪽, 직진, 오른쪽으로 가는 경우의 수 계산
'''

t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split(' '))
    matrix = list()
    available_s = list()
    result = list()
    
    for i in range(m):
        matrix.append(input())
        # ?가 나오는 행의 인덱스를 저장
        if '?' in matrix[i]:
            idx = i
            
    s = 2*d - 2
    # ?가 나오기 전 탐색
    for i in range(m-2, idx, -1):
        if s+2 < 2*n-1:
            if matrix[i][s+1] == '+':
                s += 2
                continue
        if s-2 > -1:
            if matrix[i][s-1] == '+':
                s -= 2
                continue
    # 왼쪽, 직진, 오른쪽에서 갈 수 있는 경로만 저장 
    if s+2 < 2*n-1:
        available_s.append(s+2)
    if s-2 > -1:
        available_s.append(s-2)
        
    available_s.append(s)
    
    # ? 이후 사다리타는 
    def get_start(s):
        for i in range(idx-1, -1, -1):
            if s+2 < 2*n-1:
                if matrix[i][s+1] == '+':
                    s += 2
                    continue
            if s-2 > -1:
                if matrix[i][s-1] == '+':
                    s -= 2
                    continue
        return s
    
    for i in available_s:
        tmp = get_start(i) // 2 + 1
        result.append(tmp)
        
    result.sort()
    
    for i in result:
        print(i, end=' ')
    print()
