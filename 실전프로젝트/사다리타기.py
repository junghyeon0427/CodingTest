'''
문제 상황 자체를 뒤집어서 생각
목적지 -> 출발지
'''
t = int(input())

for _ in range(t):
    # n = 시작번호의 개수
    # m = 사다리의 크기
    # d = 목적지의 위치
    n, m, d = map(int, input().split(' '))
    arr = list()
    
    for _ in range(m):
        arr.append(input())
        
    i = m - 1
    y = 2*d - 2
    w = 2*n - 2
    
    for _ in range(m):
        if 0 <= y + 1 <= w:
            if arr[i][y+1] == '+':
                y += 2
                i -=1
                continue
        if 0 <= y - 1 <= w:
            if arr[i][y-1] == '+':
                y -= 2
                i-= 1
                continue
        i -= 1
                
    print((y+2) // 2)
