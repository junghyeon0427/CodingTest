'''
별도의 알고리즘 없이 주어진 조건의 흐름대로 구현하는 문제
-> 요즘 트렌드????????
'''
def function(row, col, d):
    cnt = 0
    clean = 0

    while True:
        if matrix[row][col] == 0:
            matrix[row][col] = 2
            clean += 1

        while True:
            if cnt == 4:
                d = (d+2) % 4
                nr = row + direct[d][0]
                nc = col + direct[d][1]

                if matrix[nr][nc] == 1:
                    return clean
                else:
                    row = nr
                    col = nc
                    cnt = 0
                    d = (d+2) % 4
                break

            nr = row + direct[(d+3) % 4][0]
            nc = col + direct[(d+3) % 4][1]

            if matrix[nr][nc] == 0:
                row = nr
                col = nc
                d = (d+3) % 4
                cnt = 0
                break
            else:
                d = (d+3) % 4
                cnt += 1


t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    r, c = map(int, input().split())

    direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(function(r, c, d))
