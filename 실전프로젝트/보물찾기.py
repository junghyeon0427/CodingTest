'''
Simulation 
F = 0, R = 1, B = 2, L = 3 을 이용해서 코드 간결하게 처리 
'''

t = int(input())

for _ in range(t):
    n = int(input())

    matrix = list()
    
    for _ in range(n):
        matrix.append(list(map(str, input().split(' '))))
    
    visited = [[''] * n for _ in range(n)]
    r, c = 0, 0
    prev_direction = 'B'
    next_direction = ''
    
    while True:
        if prev_direction in visited[r][c]:
            break

        visited[r][c] += prev_direction 

        direction = matrix[r][c][:1]
        dist = int(matrix[r][c][1:])
        
        if prev_direction == 'F':
            if direction == 'F':
                next_direction = 'F'
            elif direction == 'R':
                next_direction = 'R'
            elif direction == 'L':
                next_direction = 'L'
            else:
                next_direction = 'B'

        elif prev_direction == 'R':
            if direction == 'F':
                next_direction = 'R'
            elif direction == 'R':
                next_direction = 'B'
            elif direction == 'L':
                next_direction = 'F'
            else:
                next_direction = 'L'

        elif prev_direction == 'L':
            if direction == 'F':
                next_direction = 'L'
            elif direction == 'R':
                next_direction = 'F'
            elif direction == 'L':
                next_direction = 'B'
            else:
                next_direction = 'R'

        else:
            if direction == 'F':
                next_direction = 'B'
            elif direction == 'R':
                next_direction = 'L'
            elif direction == 'L':
                next_direction = 'R'
            else:
                next_direction = 'F'

        if next_direction == 'F':
            r += dist
            prev_direction = next_direction

        elif next_direction == 'B':
            r -= dist
            prev_direction = next_direction
            
        elif next_direction == 'R':
            c += dist
            prev_direction = next_direction
            
        elif next_direction == 'L':
            c -= dist
            prev_direction = next_direction

    print(r, c)
