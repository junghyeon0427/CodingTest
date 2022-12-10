# 재귀로 구현
from collections import defaultdict


testcase = int(input())

def inorder(root):
    if tree[root]:
        inorder(tree[root][0])
        print(root, end=' ')
        inorder(tree[root][1])
        
def preorder(root):
    if tree[root]:
        print(root, end=' ')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
def postorder(root):
    if tree[root]:
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end=' ')

for _ in range(testcase):
    l = int(input())
    t = list(map(int, input().split()))
    
    tree = defaultdict(int)

    for i in range(l):
        if 2*i + 2 < l:
            tree[t[i]] = [t[2*i + 1], t[2*i + 2]]
        elif 2*i + 1 < l:
            tree[t[i]] = [t[2*i + 1], -1]
        else:
            tree[t[i]] = [-1, -1]
    
    r = t[0]
    
    inorder(r)
    del tree[-1]
    print()
    
    preorder(r)
    del tree[-1]
    print()
    
    postorder(r)
    del tree[-1]
    print()
