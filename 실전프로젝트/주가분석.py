'''
뒤에서부터 시작, 최고가 = 맨 마지막 주가
전날의 주가가 최고가보다 낮으면 그때 차이를 계산해서 저장
그렇지 않다면 최고가를 업데이트
'''

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    d = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split(' ')))
    stock = stock[::-1]
    max_price = stock[0]
    sum_price = 0
    
    for i in range(1, len(stock)):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            sum_price += (max_price-stock[i])
            
    print(sum_price)
