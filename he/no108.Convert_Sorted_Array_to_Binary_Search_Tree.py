'''
作者：jalan
链接：https: // leetcode - cn.com / problems / convert - sorted - array - to - binary - search - tree / solution / tu - jie - er - cha - sou - suo - shu - gou - zao - di - gui - python - go /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
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
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None

        # 找到中点作为根节点
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        # 左侧数组作为左子树
        left = nums[:mid]
        right = nums[mid + 1:]

        # 递归调用
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)

        return node


