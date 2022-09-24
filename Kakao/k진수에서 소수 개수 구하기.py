# 2022 KAKAO BLIND RECRUITMENT
# 로직이 어려운 문제는 아니지만, 소수 판별 함수를 작성할 때 O(logN)으로 짜야 타임아웃 x
# 변수명 좀 더 신경써서 짤 것

import math

def solution(n, k):
    answer = 0
    j = 0
    i = 1
    arr = list()
    arr2 = list()
    string = ''
    
    while i < n:
        i = k ** j
        j += 1
    j -= 2
    
    while j > 0:
        arr.append(n // (k**j))
        n -= (n // (k**j)) * (k**j)
        j -= 1
        
    arr.append(n)
    
    for i in arr:
        string += str(i)
        
    for i in string.split('0'):
        if i == '':
            continue
        arr2.append(int(i))
    
    # 소수 판별 함수
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) +1):
            if n % i == 0:
                return False
        return True
    
    for i in arr2:
        if is_prime(i):
            answer += 1
        
    return answer
