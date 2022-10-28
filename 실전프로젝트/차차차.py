'''
Dynamic Programming
dp[i][j] = max(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
j가 양 끝의 점인 경우 out of range -> 따로 처리
무지성 하드 코딩?
'''
t = int(input())

for _ in range(t):
    N = int(input())

    matrix = list()

    for _ in range(N):
        matrix.append(list(map(int, input().split(' '))))

    dp = [[0]*5 for _ in range(N)]

    for i in range(1, 4):
        if matrix[N-1][i] == 1:
            continue
        dp[N-1][i] += matrix[N-1][i-1] + matrix[N-1][i+1]

    for i in range(N-2, -1, -1):
        for j in range(5):

            if matrix[i][j] == 1:
                continue

            if 0 < j < 4:
                dp[i][j] = max(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
                if matrix[i][j-1] == 1:
                    dp[i][j] += matrix[i][j-1]
                if matrix[i][j+1] == 1:
                    dp[i][j] += matrix[i][j+1]
                if matrix[i][j] != 0:
                    dp[i][j] += matrix[i][j]

            elif j == 0:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
                if matrix[i][j+1] == 1:
                    dp[i][j] += matrix[i][j+1]
                if matrix[i][j] != 0:
                    dp[i][j] += matrix[i][j]

            elif j == 4:
                dp[i][j] = max(dp[i+1][j - 1], dp[i+1][j])
                if matrix[i][j-1] == 1:
                    dp[i][j] += matrix[i][j-1]
                if matrix[i][j] != 0:
                    dp[i][j] += matrix[i][j]

    print(max(dp[0]))
