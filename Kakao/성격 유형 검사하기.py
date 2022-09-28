from collections import defaultdict
'''
딕셔너리를 이용해서 값을 
'''
def solution(survey, choices):
    result = ''
    
    dic = defaultdict(int)
    dic['R'] = 0
    dic['T'] = 0
    dic['C'] = 0
    dic['F'] = 0
    dic['J'] = 0
    dic['M'] = 0
    dic['A'] = 0
    dic['N'] = 0
        
    for i, j in zip(survey, choices):
        if j == 4:
            continue
        elif j < 4:
            tmp = i[0]
            dic[tmp] += 4-j
            continue
        elif j > 4:
            tmp = i[1]
            dic[tmp] += j-4
            continue
            
    if dic['R'] >= dic['T']:
        result += 'R'
    if dic['R'] < dic['T']:
        result += 'T'
        
    if dic['C'] >= dic['F']:
        result += 'C'
    if dic['C'] < dic['F']:
        result += 'F'
        
    if dic['J'] >= dic['M']:
        result += 'J'
    if dic['J'] < dic['M']:
        result += 'M'
    
    if dic['A'] >= dic['N']:
        result += 'A'
    if dic['A'] < dic['N']:
        result += 'N'
        
    return result
