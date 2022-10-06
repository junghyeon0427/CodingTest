'''
2018 KAKAO BLIND RECRUITMENT
간단한 bitwise 연산 문제, 길이만 
'''

def solution(n, arr1, arr2):
    bin_arr = list()
    
    for i, j in zip(arr1, arr2):
        tmp = bin(i | j)[2:]
        while len(tmp) < n:
            tmp = '0' + tmp
        tmp = tmp.replace('1', '#', n)
        tmp = tmp.replace('0', ' ', n)
        bin_arr.append(tmp)
    
    return bin_arr
