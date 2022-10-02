'''
파이썬 기본 자료구조를 이해하고 있으면 쉽게 풀 수 있는 문제
'''
def solution(s):
    word_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num, word in enumerate(word_lst):
        s = s.replace(word, str(num))
    return int(s)
