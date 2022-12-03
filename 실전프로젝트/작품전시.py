'''
KAKAO 기출 문제인 캐시와 유사하지만 좀 더 까다로운 처리가 필요
'''
t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    
    cache = []
    result = []
    
    # cache[i][0] = count
    # cache[i][1] = 작품 번호
    for i in lst:
        flag = True
        flag2 = True
        # cache에 여유가 있는 경우
        if len(cache) < n:
            # 이미 작품 번호가 cache에 있는 경우
            for j in range(len(cache)):
                if cache[j][1] == i:
                    cache[j][0] += 1
                    cache.sort(reverse=True, key=lambda x: x[0])
                    flag = False
                    break
            # flag = True -> 작품 번호가 cache에 없으므로 추가
            if flag:
                cache.append([1, i])
        # cache가 꽉 찬 경우
        else:
            # 이미 작품 번호가 cache에 있는 경우
            for j in range(len(cache)):
                if cache[j][1] == i:
                    cache[j][0] += 1
                    cache.sort(reverse=True, key=lambda x: x[0])
                    flag2 = False
                    break
            # flag2 = True -> 작품 번호가 cache에 없으므로 추가
            if flag2:
                min_num = min(cache)[0]
                for j in range(len(cache)):
                    if cache[j][0] == min_num:
                        cache.remove(cache[j])
                        break
                cache.append([1, i])
                
    for i in cache:
        result.append(i[1])
    
    result.sort()
    
    for i in result:
        print(i, end=' ')
    print()
