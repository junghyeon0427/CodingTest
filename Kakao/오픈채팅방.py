'''
2019 KAKAO BLIND RECRUITMENT
stack에 Enter/Leave와 id를 기록한다.
dictionary를 이용하여 이름이 바뀔때마다 바뀐 이름 값 저장
stack에서 원소들을 꺼내며 id에 해당하는 딕셔너리의 value값으로 치환
'''
def solution(record):
    new_record = list()
    
    for i in record:
        new_record.append(i.split(' '))
    
    stk = list()
    dic = dict()
    
    for i in new_record:
        if i[0] == 'Enter':
            stk.append([i[0], i[1]])
            # dic에 이름을 계속 업데이트
            dic[i[1]] = i[2]
        elif i[0] == 'Leave':
            stk.append([i[0], i[1]])
        elif i[0] == 'Change':
            # dic에 이름을 계속 업데이트
            dic[i[1]] = i[2]
    
    result = list()
        
    # dic에 저장된 이름 -> 가장 마지막으로 변경한 
    for i in stk:
        tmp = ''
        if i[0] == 'Enter':
            tmp = dic[i[1]] + '님이 들어왔습니다.'
            result.append(tmp)
        elif i[0] == 'Leave':
            tmp = dic[i[1]] + '님이 나갔습니다.'
            result.append(tmp)
            
    return result
