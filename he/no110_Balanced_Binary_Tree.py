# 注释的方法没有网上的优
# 注意本题标签深度搜索算法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.right = self.right
            self.right = t

    def getRight(self) -> 'TreeNode':
        return self.right

    def getLeft(self) -> 'TreeNode':
        return self.left

    def setRootVal(self, obj):
        self.val = obj

    def getRootVal(self):
        return self.val


# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
#         if abs(self.maxDepth(root.left)-self.maxDepth(root.right))<2:
#             return self.isBalanced(root.right) and self.isBalanced(root.left)
#         else:
#             return False
#
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         else:
#             left_height = self.maxDepth(root.left)
#             right_height = self.maxDepth(root.right)
#             return max(left_height, right_height) + 1

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        # 该方法具有减枝功能
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。