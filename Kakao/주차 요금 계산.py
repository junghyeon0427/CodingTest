from collections import defaultdict

'''
문제 자체는 간단하지만, 입력값 전처리 및 나머지 조건이 까다로운 문제
1. 딕셔너리를 이용해서 차량번호에 따른 누적 주차 시간을 구한다.
2. 별도의 비용을 구하는 함수를 이용해서 누적 주차 시간에 따른 비용을 계산한다.
3. 차량번호를 기준으로 정렬해서 결과값 리턴
'''
def solution(fees, records):
    new_records = list()
    
    # 입력값 전처리
    for i in records:
        new_records.append(i.split(' '))
    
    dictionary = dict()
    d = defaultdict(int)
    
    time = 0
    result = list()
    
    # OUT인 경우에 d 딕셔너리에 누적 시간을 계속 더해준다.
    for i in new_records:
        time = 0
        sum_fee = 0
        if i[2] == 'IN':
            dictionary[i[1]] = i[0]
        else:
            tmp = dictionary[i[1]].split(':')
            tmp2 = i[0].split(':')
            time += (int(tmp2[0]) - int(tmp[0])) * 60
            time += int(tmp2[1]) - int(tmp[1])
            d[i[1]] += time
            # del 없이 하나의 딕셔너리 만으로 해결할 수 있을수도
            del dictionary[i[1]]
    
    # dictionary에 남아있다 -> 입차만 하고 출차는 하지 x
    for i, j in dictionary.items():
        t = 0
        tmp = j.split(':')
        tmp2 = ['23', '59']
        t += (int(tmp2[0]) - int(tmp[0])) * 60
        t += int(tmp2[1]) - int(tmp[1])
        d[i] += t
    
    # 비용을 구하는 함수
    def get_fee(time, fees):
        sum_fee = 0
        if time > fees[0]:
            # 올림을 해주기 위해 0.5를 더해준다.
            sum_fee += fees[1] + int(((time - fees[0] + fees[2] - 0.5) // fees[2]) * fees[3])
        else:
            sum_fee = fees[1]
        return sum_fee
        
    for i, j in d.items():
        result.append([i, get_fee(j, fees)])
        
    result.sort()
    
    ret = list()
    
    for i in result:
        ret.append(i[1])
        
    return ret
