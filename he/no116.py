"""
填充每个节点的下一个右侧节点指针
参考：https://medium.com/@desolution/從leetcode學演算法-84-tree-11-dfs-8-2bebed74524d
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        if root.left: root.left.next = root.right
        if root.right and root.next: root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level_first = root
        while level_first:
            curr = level_first
            while curr:
                if curr.left: curr.left.next = curr.right
                if curr.right and curr.next: curr.right.next = curr.next.left
                curr = curr.next
            level_first = level_first.left
        return root
'''