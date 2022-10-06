'''
2019 카카오 개발자 겨울 인턴십
전처리를 통해 정수만 담긴 리스트로 바꿔준 다음 Counter를 이용해서 빈도수 계산
'''
from collections import Counter


def solution(s):
    # 특이 케이스 처리
    if len(s) == 1:
        return [int(s[2:-2])]
    
    # 정수 리스트로 바꿔주는 작업
    tmp_s = s[2:-2].split('},{')
    new_s = list()
    result = list()
    
    for i in tmp_s:
        if ',' not in i:
            new_s.append(int(i))
        else:
            tmp = i.split(',')
            for j in tmp:
                new_s.append(int(j))
    
    cnt = Counter(new_s)
    cnt_sort = cnt.most_common()
    
    for i in cnt_sort:
        result.append(i[0])
    
    return result
