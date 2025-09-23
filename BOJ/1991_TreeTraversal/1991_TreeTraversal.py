def preorder_traversal(node) -> None:    
    if node == '.': return # Base Case
    print(node, end="")
    preorder_traversal(tree[node][0])  
    preorder_traversal(tree[node][1])  

def inorder_traversal(node) -> None:    
    if node == '.': return # Base Case
    inorder_traversal(tree[node][0])
    print(node, end="")
    inorder_traversal(tree[node][1])

def postorder_traversal(node) -> None:    
    if node == '.': return # Base Case
    postorder_traversal(tree[node][0])
    postorder_traversal(tree[node][1])
    print(node, end="")

import sys
input = sys.stdin.readline
n = int(input().strip())

tree = {}  # 전역변수 tree

for i in range(n):
    datas = input().strip().split()
    tree[datas[0]] = (datas[1], datas[2])


root = 'A' 
preorder_traversal(root)    # 전위 순회
print('')                   # \n

inorder_traversal(root)     # 중위 순회
print('')                   # \n

postorder_traversal(root)   # 후위 순회
print('')                   # \n