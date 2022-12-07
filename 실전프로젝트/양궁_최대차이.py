# 최대차이로 이기는 점수만 계산
t = int(input())

for _ in range(t):
    score = list(map(int, input().split()))

    n = score[0]
    score = score[1:]

    # 1 -> 한국이 이기는 경우
    # 0 -> 미국이 이기는 경우
    binary_list = list()
    array = [0] * 11
  
    def explore(tmp=array, idx=0):
        if idx > 10:
            if sum(tmp) <= n:
                binary_list.append(tmp)
            return

        tmp2 = tmp[:]
        tmp2[idx] = 1
        explore(tmp2, idx+1)
        tmp3 = tmp[:]
        explore(tmp3, idx+1)

    def get_score(k_lst, a_lst, k_score=0, a_score=0):
        s = 10
        for i, j in zip(k_lst, a_lst):
            if i > j:
                k_score += s
            elif j != 0:
                a_score += s
            s -= 1
        return k_score, a_score

    explore()

    result = []

    for i in range(len(binary_list)):
        tmp_list = [0] * 11
        cnt = 0
        k_score = 0
        a_score = 0
        for j in range(11):
            if binary_list[i][j] == 1:
                cnt += score[j] + 1
                if cnt <= n:
                    tmp_list[j] = score[j] + 1
        k, a = get_score(tmp_list, score)
        if [k-a, k] in result:
            continue
        if k-a < 0:
            continue
        result.append([k-a, k])

    result.sort(reverse=True)

    if len(result) == 0:
        print(-1)
    else:
        print(result[0][1])
