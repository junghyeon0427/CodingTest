'''
2018 KAKAO BLIND RECRUITMENT
문제가 말하고자 하는것이 무엇인지 파악하면 쉽게 구현 가능
'''

def solution(s):
    result = list()
    pointer = 0
    idx = 26
    # 기존의 단어 딕셔너리를 만들어준다.
    word_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 
                 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 
                 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 
                 'R':18, 'S':19, 'T':20, 'U':21, 'V':22,
                 'W':23, 'X':24, 'Y':25, 'Z':26}
      
    while pointer < len(s):
        # 현재 포인터에 해당하는 스트링을 가져오고
        tmp = s[pointer]
        # 해당 단어가 사전에 없을때까지 계속 한단어씩 붙인다.
        while tmp in word_dict:
            pointer += 1
            if pointer > len(s)-1:
                break
            tmp += s[pointer]
        # 사전에 없다 -> 새로 사전에 추가를 해줘야함
        # 사전에 추가하기전에 있던 단어의 사전 인덱스 값을 tmp2에 넣어 result에 저장
        tmp2 = tmp[:-1]
        if pointer == len(s):
            result.append(word_dict[tmp])
            break
        result.append(word_dict[tmp2])
        idx += 1
        # tmp -> 새로운 단어이므로 27번 인덱스부터 채워준다.
        word_dict[tmp] = idx
        
    return result
