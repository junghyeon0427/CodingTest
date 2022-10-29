'''
1. 모든 배열의 처음 크기는 ‘0’ 이다.
2. 원소가 추가될 때, 추가될 원소를 포함한 전체 원소의 수가 배열의 크기보다 작거나 같은 경우 기존배열에 원소를 추가한다.
3. 원소가 추가될 때, 추가될 원소를 포함한 전체 원소의 수가 배열의 크기를 넘는 경우 새로운 배열을 만들고 값을 복사한다. 
4. 이때, 새로 만든 배열의 크기는 전체 원소 수보다 큰 2의 거듭제곱 수 중 가장 작은 값으로 한다. 

-> 배열 인덱스 값에 빨리 접근하기 위해 딕셔너리 사용
dict1 : arr의 크기
dict2 : 남은(사용 가능한) arr의 크기
'''
from collections import defaultdict


t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list()
    
    for _ in range(n):
        arr.append(list(map(int, input().split(' '))))
        
    result = 0
    # arrray의 크기
    dict1 = defaultdict(int)
    # 남은 array의 크기
    dict2 = defaultdict(int)

    for num, size in arr:
        i = 1
        j = 1
        while 2 ** i <= size:
            i += 1
        if num not in dict1:
            dict1[num] = 2 ** i
            dict2[num] = dict1[num] - size
        else:
            if dict2[num] >= size:
                dict2[num] -= size
            else:
                tmp = dict1[num] - dict2[num]
                while 2 ** j <= tmp+size:
                    j += 1
                dict1[num] = 2 ** j
                dict2[num] = dict1[num] - (tmp+size)
                result += tmp

    print(result)
