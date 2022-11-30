'''
padding을 추가하고 반복문으로 conv 연산 진행
'''
t = int(input())

for _ in range(t):
    h, w = list(map(int, input().split()))
    
    matrix = [[0] * (w+2) for _ in range(h+2)]
    result = [[0] * w for _ in range(h)]
    mat = []
    
    for _ in range(h):
        mat.append(list(map(int, input().split())))
    
    for i in range(1, h+1):
        for j in range(1, w+1):
            matrix[i][j] = mat[i-1][j-1]
    
    # 모서리 부분 padding
    matrix[0][0] = mat[0][0]
    matrix[0][-1] = mat[0][-1]
    matrix[-1][0] = mat[-1][0]
    matrix[-1][-1] = mat[-1][-1]
    
    # padding
    for i in range(1, h+1):
        matrix[i][0] = matrix[i][1]
        matrix[i][-1] = matrix[i][-2]
    for i in range(1, w+1):
        matrix[0][i] = matrix[1][i]
        matrix[-1][i] = matrix[-2][i]
    
    for i in range(1, h+1):
        for j in range(1, w+1):
            # sum(matrix[i-1][j-1:j+2]) + sum(matrix[i][j-1:j+2]) + sum(matrix[i+1][j-1:j+2])
            tmp = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + \
                    matrix[i][j-1] + matrix[i][j] + matrix[i][j+1]+ \
                    matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]
            result[i-1][j-1] = tmp // 9
    
    print(h, w)
    
    for res in result:
        for i in res:
            print(i, end=' ')
        print()
