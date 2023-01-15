'''
꼭짓점을 제외한 나머지 점들은 짝수번 등장해야함
넓이 비교 -> 꼭짓점의 등장 횟수 비교
'''
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles):
        direct = defaultdict(int)        
        x = float('inf')
        a = float('-inf')
        y = float('inf')
        b = float('-inf')

        for rectangle in rectangles:
            x1, y1, a1, b1 = rectangle
            x = min(x, x1)
            a = max(a, a1)
            y = min(y, y1)
            b = max(b, b1)

        total_area = 0

        for rectangle in rectangles:
            x1, y1, a1, b1 = rectangle
            total_area += (a1 - x1) * (b1 - y1)
            direct[(x1, y1)] += 1
            direct[(x1, b1)] += 1
            direct[(a1, b1)] += 1
            direct[(a1, y1)] += 1
                
        # 사각형들의 합이 전체 사각형의 합과 다른경우 -> prefect rectangle x

        if total_area != (a-x) * (b-y):
            return False
        
        # 꼭짓점의 경우 +1을 해주어 2로 만듦
        direct[(x, y)] += 1
        direct[(x, b)] += 1
        direct[(a, b)] += 1
        direct[(a, y)] += 1
         
        # 홀수번이 한번이라도 등장하면 prefect rectangle x
        for i in direct.values():
            if i % 2 != 0:
                return False
        
        return True
