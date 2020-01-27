'''
作者：Yuanye He
力扣原题解法参考链接：https: // leetcode - cn.com / problems / maximum - depth - of - binary - tree / solution / er - cha - shu - de - zui - da - shen - du - by - leetcode /
增添TreeNode类，以供线下测试
'''
# Definition for a binary tree node.
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

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

if __name__ == '__main__':
    # [3,9,20,null,null,15,7] 怎么输入列表直接初始化一个二叉树
    root = TreeNode(3)  # How to init a Tree
    root.insertLeft(9)
    root.insertRight(20)
    right = root.getRight()

    right.insertLeft(15)
    right.insertRight(7)
    answer = Solution()
    print(answer.maxDepth(root))

