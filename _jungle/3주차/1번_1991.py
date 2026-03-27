# 1991 - 트리 순회 / 1번
class TreeNode:
    
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
    
# 부모 - 왼 - 오    
def pre_ord(node):
    if node is None:
        return 
    
    print(node.data,end='')
    pre_ord(node.left)
    pre_ord(node.right)

# 왼 - 부모 - 오
def in_ord(node):
    if node is None:
        return
    
    in_ord(node.left)
    print(node.data,end='')
    in_ord(node.right)
    
    
# 왼 - 오 - 부모
def post_ord(node):
    if node is None:
        return
    
    post_ord(node.left)
    post_ord(node.right)
    print(node.data,end='')
#################################
N =int(input())
nodes = {}

for _ in range(N):
    parent, left, right = input().split()

    if parent not in nodes:
        nodes[parent]=TreeNode(parent)
    
    if left !='.' : 
        if left not in nodes:
            nodes[left]=TreeNode(left)
        
        nodes[parent].left = nodes[left]

    if right !='.':
        if right not in nodes:
            nodes[right]=TreeNode(right)
            
        nodes[parent].right = nodes[right]
        
# 대부분 트리문제에서 루트는 'A' 로 주어지므로 이렇게 호출
root = nodes['A']

pre_ord(root)
print()
in_ord(root)
print()
post_ord(root)