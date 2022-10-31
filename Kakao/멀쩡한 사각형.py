'''
Summer/Winter Coding(2019)
y = ax 함수를 정의하고 각 포인트마다 가질수있는 최대 사각형의 크기 계산
gcd를 이용해서 계산량 최소화
'''
def solution(w,h):
    result = 0
    
    # 작은 값을 기준으로 계산
    if w > h:
        tmp = h
        h = w
        w = tmp
    
    def get_gcd(x, y):
        if y == 0:
            return x
        else:
            return get_gcd(y, x % y)
    
    def func(x):
        return (h/w) * x
    
    gcd = get_gcd(h, w)
    
    new_H = h // gcd
    new_W = w // gcd
    
    for i in range(1, new_W):
        result += int(func(i))
        
    return (h*w) - gcd * ((new_H*new_W) - (2*result))
