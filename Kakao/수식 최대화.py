'''
2020 카카오 인턴십
연산자 경우의 수 : 6, expression의 최대 길이가 100이므로 bruteforce
'''
def solution(expression):
    idx = 0
    result = list()
    ex_list = list()
    op_list = [['-', '*', '+'], ['-', '+', '*'], ['+', '-', '*'], 
               ['+', '*', '-'], ['*', '+', '-'], ['*', '-', '+']]
    
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '*' or expression[i] == '-':
            ex_list.append(expression[idx:i])
            ex_list.append(expression[i])
            idx = i+1

    ex_list.append(expression[idx:])
    
    # 연산자 순서에 맞게 연산을 하고 리스트 
    for i in op_list:
        list_cp = ex_list[:]
        for j in i:
            k = 0
            while k < len(list_cp):
                if list_cp[k] == j:
                    list_cp[k] = str(eval(list_cp[k-1] + list_cp[k] + list_cp[k+1]))
                    list_cp = list_cp[:k-1] + [list_cp[k]] + list_cp[k+2:]
                    continue
                k += 1
        result.append(abs(int(list_cp[0])))
    
    return max(result)
