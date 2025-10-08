import sys
N = int(input().strip())
graph = {}

def preorder(root) -> str:
    if root == '.': 
        return ""
    return root + preorder(graph[root][0]) + preorder(graph[root][1])

def inorder(root) -> str:
    if root == '.': 
        return ""
    return inorder(graph[root][0]) + root + inorder(graph[root][1])

def postorder(root) -> str:
    if root == '.': 
        return ""
    return postorder(graph[root][0]) + postorder(graph[root][1]) + root

for _ in range(N):
    parent, left, right = map(str, input().strip().split())
    graph[parent] = (left, right)

for f in (preorder, inorder, postorder):
    print(f('A'))