'''
2019 KAKAO BLIND RECRUITMENT
데이터베이스에서 유일성과 최소성을 만족시키는 키값을 찾는 문제
배열에서 pk를 먼저 제거하고 이후 과정을 진행하려고 했으나 오히려 꼬여버림
-> col의 길이가 8 이하이므로 모든 배열에서 1 ~ len(col)까지 모든 조합의 수를 저장
이후 집합을 이용해서 유일성과 최소성을 만족하는 키 배열 저장

+ 코드, 변수명을 좀 더 간결하게 짜기... 불필요한 코드가 많아 보임
'''

import itertools


def solution(relation):
    new_relation = list()
    tmp_list = list()
    idx = list()
    
    # 배열을 90도 회전
    for i in range(len(relation[0])):
        for j in range(len(relation)):
            tmp_list.append(relation[j][i])
        new_relation.append(tmp_list)
        tmp_list = list()
    
    # 인덱스 생성
    idx = [i for i in range(len(new_relation))]

    comb = list()
    comb_flatten = list()

    for j in range(1, len(new_relation)+1):
        comb.append(list(itertools.combinations(idx, j)))
    
    # l -> a 1차원으로 펴준다
    for i in range(len(comb)):
        for j in range(len(comb[i])):
            comb_flatten.append(comb[i][j])
    
    tmp = list()
    tmp2 = list()
    result_tmp = list()
    
    flag = True
    
    # 유일성과 최소성 처리
    # 유일성 확인 -> 최소성 확인 순으로 진행
    for i in comb_flatten:
        s = set()
        for j in i:
            tmp.append(new_relation[j][:])
        for x in range(len(new_relation[0])):
            for y in range(len(tmp)):
                 tmp2.append(tmp[y][x])
            s.add(tuple(tmp2))
            tmp2 = list()
        # 유일성을 만족하는 경우
        if len(s) == len(new_relation[0]):
            if len(result_tmp) == 0:
                result_tmp.append(i)
            else:
                for k in result_tmp:
                    # flag == False 이면 최소성을 만족 x
                    if len(set(k) - set(i)) == 0:
                        flag = False
                if flag:
                    result_tmp.append(i)
        flag = True
        tmp = list()
    return len(result_tmp)
