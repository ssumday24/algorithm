#5639 - 이진 검색 트리 BST
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,value):
        self.value = value
        self.left =None
        self.right =None

#후위 순회 
def post_ord(node):
    if node is None:
        return # 종료조건
    
    post_ord(node.left)
    post_ord(node.right)
    print(node.value)
   
def insert(root, value):
    p = root
    while True:
        if value < p.value:
            if p.left is None:
                p.left = Node(value)
                return
            else:
                p = p.left
        else:
            if p.right is None:
                p.right = Node(value)
                return
            else:
                p = p.right
##########################################
root = None


#입력이 끝날 때까지(EOL 또는 EOF) 계속 반복.

for line in sys.stdin:
    if not line.strip():
        continue
    n = int(line.strip())
    if root is None:
        root = Node(n)
    else:
        insert(root, n)


post_ord(root)