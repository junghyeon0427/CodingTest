'''
2018 KAKAO BLIND RECRUITMENT
deque를 이용해서 해결, cache hit이 일어나면 무조건 que에서 제거하고 새로 넣어야함
'''

from collections import deque


def solution(cacheSize, cities):
    time = 0
    cache = deque()
    
    for i in cities:
        i = i.lower()
        if len(cache) < cacheSize:
            # cache hit
            if i in cache:
                cache.remove(i)
                cache.append(i)
                time += 1
                continue
            # cache miss
            cache.append(i)
            time += 5
            continue
        # cache hit
        if i in cache:
            cache.remove(i)
            cache.append(i)
            time += 1
        # cache miss
        else:
            # cache size =0 -> 항상 cache miss
            if cacheSize == 0:
                time += 5
                continue
            # LRU
            cache.popleft()
            time += 5
            cache.append(i)
            
    return time
