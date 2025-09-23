import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
preorder = list(map(int, sys.stdin.read().split()))

def fun_preorder(start, end):
    if start >= end:
        return

    root = preorder[start]
    idx = start + 1

    while idx < end and preorder[idx] < root:
        idx += 1
    
    fun_preorder(start + 1, idx)
    fun_preorder(idx, end)
    print(root)
fun_preorder(0, len(preorder))