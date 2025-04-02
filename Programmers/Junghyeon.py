# que를 사용한 빡구현 문제

from collections import deque

def solution(players, m, k):
    answer = 0
    
    server_list = deque([])
    
    for time, player in enumerate(players):
        # n : 필요한 서버
        n = player // m
        
        # 서버가 존재한다면
        # 한시간씩 증가, 만약 k에 도달하면 popleft()
        if server_list:
            for i in range(len(server_list)):
                server_list[i] += 1
                server_list[i] %= k+1
        
        new_server_list = deque([])
        # 0인 서버 (찌꺼기) 제거 프로세스
        for i in range(len(server_list)):
            if server_list[i] != 0:
                new_server_list.append(server_list[i])
        
        server_list = new_server_list
        
        # 서버가 필요한 상황
        # 부족한 만큼 초기화
        if n > len(server_list):
            for _ in range(n-len(server_list)):
                server_list.append(1)
                answer += 1
        
        print(f"{time}~{time+1}, {n}, {answer}")
        print(server_list)
        print()
        
    return answer
