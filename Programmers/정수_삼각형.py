# DP : 삼각형을 2차원 배열로 생각
# idx가 0 혹은 len이면, case는 1개 / 나머지의 경우에는 case 2개 (max 처리)

def solution(triangle):
    
    height = len(triangle[-1])
    array = [[0] * height for _ in range(height)]
    
    for i in range(height):
        if i == 0:
            array[i][i] = triangle[i][i]
        else:
            for j in range(i+1):
                if j == 0:
                    array[i][j] = triangle[i][j] + array[i-1][j]
                elif j == i:
                    array[i][j] = triangle[i][j] + array[i-1][j-1]
                else:
                    array[i][j] = triangle[i][j] + max(array[i-1][j-1], array[i-1][j])
    
    return max(array[-1])
