t = int(input())

for _ in range(t):
    num_list = list(map(int, input().split()))
    n = num_list[0]
    num_list = num_list[1:]
    result = list()
    
    for i in range(n):
        cnt = 0
        idx = 0
        while True:
            # 찾고자하는 num인 경우에 break
            if num_list[idx] == i+1:
                 break
            # i보다 큰 값이면 cnt 증가
            if num_list[idx] > i:
                cnt += 1
            idx += 1
        result.append(cnt)
        '''
        result에 넣고 다시 루프를 돌며 리턴하는것 보다
        cnt를 출력하는게 좀 더 효율적
        '''
        # print(cnt, end=' ')
    # print()
         
    for i in result:
        print(i, end=' ')
    print()
    
