'''
Summer/Winter Coding(~2018)
다익스트라
'''
import heapq


def solution(N, road, K):
    
    graph = [[] for _ in range(N+1)]
    distance = [float('inf')] * (N+1)
    
    # 입력값을 다루기 쉽게 전처리, 양방향 그래프
    for i in road:
        # (dest, cost)로 기록
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))    
    
    def dijkstra(start):
        que = list()
        heapq.heappush(que, (0, start))
        distance[start] = 0

        while que:
            dist, now = heapq.heappop(que)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                # i[0] -> dest, i[1] -> cost
                # dist+i[1] : 새로운 cost, distance[i[0]] : 기존의 cost 
                if dist+i[1] < distance[i[0]]:
                    distance[i[0]] = dist+i[1]
                    heapq.heappush(que, (dist+i[1], i[0]))
    
    dijkstra(1)
    
    # list comprehension -> list에서 특정 값 이하의 값만 추출
    return len([i for i in distance if i <=K])
