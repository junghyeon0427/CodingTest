t = int(input())

for _ in range(t):
    n, p = map(int, input().split(' '))
    cnt = 0
    while n > 0:
        if n-2 == p:
            n -= 1
            cnt += 1
        else:
            n -= 2
            cnt += 1
    print(cnt)
