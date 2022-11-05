'''
2021 Dev-Matching: 웹 백엔드 개발자(상반기)
인덱스처리가 까다로워서 반복문으로 회전해야할 값들을 리스트에 넣고 슬라이싱으로 회전
이후 한번 더 반복문을 돌면서 리스트의 값으로 업데이트
time limit 조건을 까다롭게 걸면 실패할만한 코드..//
한번의 반복문으로 값 업데이트 + 
'''
def solution(rows, columns, queries):
    matrix = [[0]*columns for _ in range(rows)]
    result = list()
    cnt = 1
    
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = cnt
            cnt += 1
    
    for s_r, s_c, d_r, d_c in queries:
        mat_tmp = list()
        c = d_c - s_c
        c2 = c
        c3 = c
        c4 = c

        r = d_r - s_r
        r2 = r
        r3 = r
        r4 = r

        idx = 0

        s_r -= 1
        s_r2 = s_r
        s_c -= 1
        s_c2 = s_c
        d_r -= 1
        d_c -= 1

        # 회전해야할 값들 저장
        while c:
            mat_tmp.append(matrix[s_r][s_c])
            s_c += 1
            c -= 1
        while r:
            mat_tmp.append(matrix[s_r][s_c])
            s_r += 1
            r -= 1
        while c2:
            mat_tmp.append(matrix[s_r][s_c])
            s_c -= 1
            c2 -= 1
        while r2:
            mat_tmp.append(matrix[s_r][s_c])
            s_r -= 1
            r2 -= 1
        
        # 회전해야할 값들 중에서 최솟값을 저장
        result.append(min(mat_tmp))
        # 회전 과정
        mat_tmp = [mat_tmp[-1]] + mat_tmp[:-1]

        # 회전된 리스트로 업데이트
        while c3:
            matrix[s_r2][s_c2] = mat_tmp[idx]
            s_c2 += 1
            c3 -= 1
            idx += 1
        while r3:
            matrix[s_r2][s_c2] = mat_tmp[idx]
            s_r2 += 1
            r3 -= 1
            idx += 1
        while c4:
            matrix[s_r2][s_c2] = mat_tmp[idx]
            s_c2 -= 1
            c4 -= 1
            idx += 1
        while r4:
            matrix[s_r2][s_c2] = mat_tmp[idx]
            s_r2 -= 1
            r4 -= 1
            idx += 1
            
    return result
