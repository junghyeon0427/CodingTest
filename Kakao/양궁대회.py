'''
2022 KAKAO BLIND RECRUITMENT
매 순간 최대 점수를 얻는 경우를 생각하는 Greedy 문제라고 생각했지만
점수의 차이가 최대인 경우가 여러개일때 가장 낮은 점수를 더 많이 맞힌 경우를 리턴해야함 -> Greedy (x)
+++ 특정 점수를 가져오기 위해 어피치의 화살 + 1 or 0 으로 설정하는 아이디어 -> Greedy 라고 생각해도 되는지...?
info의 길이가 10밖에 안되므로 완전탐색으로 풀이하고자 생각
모든 점수마다의 경우는 라이언이 이기거나, 어피치가 이기거나 두가지의 경우밖에 없음
라이언이 이기는 경우에는 무조건 어피치의 화살 + 1만 해주면 됨
어피치가 이기는 경우 = 1, 라이언이 이기는 경우 = 0 인 길이가 11인 배열을 생성
[0,0,0, ..., 0] -> [1,1,1, ..., 1]인 배열을 만들고(2^11가지의 경우)
모든 배열을 get_score 함수에 넣어주면서 라이언이 이겼을 때, 각각의 info를 업데이트
이후에 어피치와 라이언의 점수를 계산해서 둘의 차이와 그때의 lion_info를 리턴
최댓값이 0인 경우 -> 절대 라이언은 이길 수 없다.
최댓값의 경우가 여러개인 경우 정렬 과정을 거쳐 하나의 답을 골라준다.
'''
import copy


def solution(n, info):
    binary_list = list()
    array = [0] * 11
    
    # 가능한 모든 배열을 만드는 과정
    def explore(tmp=array, idx=0):
        if idx > 10:
            binary_list.append(tmp)            
            return

        tmp2 = tmp.copy()
        tmp2[idx] = 1
        explore(tmp2, idx+1)
        tmp3 = tmp.copy()
        explore(tmp3, idx+1)

    explore()
    
    # 이긴 사람이 누구인지 배열을 입력받아 그때의 점수를 계산
    def get_score(n, info, arr, lion_info):
        apeach_info = copy.copy(info)
        lion_score = 0
        apeach_score = 0
        s1 = 10
        s2 = 10
        for k in range(len(arr)):
            # 라이언이 이긴경우
            if arr[k] == 0:
                # 화살이 남아있지 않다 -> 불가능한 경우이므로 0을 리턴
                if n < apeach_info[k] + 1:
                    return [0, lion_info]
                # lion_info에 어피치의 화살 + 1의 값을 더해준다.
                else:
                    lion_info[k] = apeach_info[k] +1
                    # 화살의 개수를 줄여주기
                    n = n - apeach_info[k] - 1
                    # apeach_info 업데이트
                    apeach_info[k] = 0
        # 라이언 점수 계산
        for x in lion_info:
            if x != 0:
                lion_score += s1
            s1 -= 1
        # 어피치 점수 계산
        for y in apeach_info:
            if y != 0:
                apeach_score += s2
            s2 -= 1
        # 남은 화살은 다 0점에 쏴준다
        lion_info[-1] = n
        return [lion_score - apeach_score, lion_info]
    
    result_tmp = list()
    result = list()
    
    for i in binary_list:
        lion_info = [0] * 11
        result_tmp.append(get_score(n, info, i, lion_info))
    
    # 라이언이 이길 수 없는 경우
    if max(result_tmp)[0] <= 0:
        return [-1]
    
    for i in result_tmp:
        if i[0] == max(result_tmp)[0]:
            result.append(i)
    
    # 최고점의 경우가 여러개일때 후처리
    if len(result) > 1:
        tmp_list = list()
        for i in range(len(result)):
            for j in range(10, -1, -1):
                if result[i][1][j] != 0:
                    tmp_list.append([j, result[i][1][j], i])
                    break
        tmp_list.sort(key=lambda x:(x[0], x[1]), reverse=True)
        return result[tmp_list[0][2]][1]
    
    return result[0][1]
