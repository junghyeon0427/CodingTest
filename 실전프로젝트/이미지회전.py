'''
Simulation
이미지를 90도 회전하는 함수 정의 후, 각도에 맞게 회전을 반복해준다.
'''

def rotate(pixel_map, n, arr):
    tmp = ''
    for i in range(n):
        for j in range(n):
            tmp += pixel_map[j][i]
        arr.append(tmp[::-1])
        tmp = ''
        
    return arr

t = int(input())


for _ in range(t):
    n, a = map(int, input().split(' '))
    
    pixel_map = list()
    arr = list()
    result = list()
    
    for _ in range(n):
        pixel_map.append(input())
        
    if a == 0:
        for i in range(n):
            print(pixel_map[i][:])
            continue
            
    elif a == 90 or a == -270:
        result = rotate(pixel_map, n, arr)
        for i in range(n):
            print(result[i][:])
            continue
            
    elif a == 180 or a == -180:
        result = rotate(pixel_map, n, arr)
        # result = rotate(result, n, arr=[]) 
        arr = list()
        result = rotate(result, n, arr)
        for i in range(n):
            print(result[i][:])
            continue
            
    else:
        result = rotate(pixel_map, n, arr)
        arr = list()
        result = rotate(result, n, arr)
        arr = list()
        result = rotate(result, n, arr)
        for i in range(n):
            print(result[i][:])
            continue
