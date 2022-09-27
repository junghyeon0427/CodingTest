from collections import deque
'''
deque를 이용해서 투 포인터를 옮겨가며 해결하는 문제
'''

def solution(queue1, queue2):
    if sum(queue1) > sum(queue2):
        max_dq = deque(queue1)
        min_dq = deque(queue2)
    else:
        max_dq = deque(queue2)
        min_dq = deque(queue1)
    
    if (sum(max_dq) + sum(min_dq)) // 2 != (sum(max_dq) + sum(min_dq)) / 2:
        return -1
    
    cnt = 0
    tmp = 0
    gap = (sum(max_dq) - sum(min_dq)) // 2
    
    # max length를 2 * len(dq)가 아닌 3 * len(dq)로 하는 이유...?
    length = 3 * len(max_dq)
     
    while (tmp != gap and cnt < length):
        if gap > tmp:
            t = max_dq.popleft()
            tmp += t
            min_dq.append(t)
            cnt += 1
        else:
            t2 = min_dq.popleft()
            tmp -= t2
            max_dq.append(t2)
            cnt += 1
    
    if sum(min_dq) != sum(max_dq):
        return -1
    
    return cnt
