# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
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
    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     if not root:
    #         return 0
    #     gap = sum - root.val
    #     count = 0
    #     if gap == 0:return count+1
    #     if root.left:
    #         count+=self.pathSum(root.left,sum)
    #         count+=self.pathSum(root.left,gap)
    #     if root.right:
    #         count += self.pathSum(root.right, sum)
    #         count += self.pathSum(root.right, gap)
    #     # if not root.right and not root.left:
    #
    #     return count

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.paths(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
    def paths(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        gap = sum - root.val
        count = 0
        if gap == 0:count= count+1
        count += self.paths(root.left, gap)
        count += self.paths(root.right, gap)
        return count






    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     paths = self.binaryTreePaths(root)
    #
    #     count = 0
    #     for i in paths:
    #         print(i)
    #         i = [int(j) for j in i.split()]
    #         for ind in range(len(i)):
    #             count = self.isSum(i[ind:],sum,count)
    #     return count
    #
    # def isSum(self, path: List[int], sum: int, count: int) -> int:
    #     path_sum = []
    #     s = 0
    #     for i in range(len(path)):
    #         s+=path[i]
    #         path_sum.append(s)
    #     print(path_sum)
    #     for i in path_sum:
    #         if i == sum:count+=1
    #     return count
    #
    # def construct_paths(self, root: TreeNode, path: str, paths: List[str]):
    #     # 列表paths是一个引用
    #     if root:
    #         path=path+' '+str(root.val)
    #         if not root.left and not root.right:  # 当前节点是叶子节点
    #             paths.append(path)  # 把路径加入到答案中
    #             # print(paths)
    #         else:
    #
    #             self.construct_paths(root.left, path, paths)
    #             self.construct_paths(root.right, path, paths)
    #
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #     paths = []
    #     self.construct_paths(root, '', paths)
    #     return paths

    # def binaryTreePaths2(self, root: TreeNode) -> List[str]:
    #     if not root:
    #         return []
    #     paths = []
    #     allNodes = []    # stack
    #     allNodes.append((root,str(root.val))) # stack把路径和节点绑定在一起
    #
    #     while(allNodes != []):
    #         i,tmp=allNodes.pop()
    #         if i.left:
    #             path =tmp+"->"+str(i.left.val)
    #             allNodes.append((i.left,path))
    #
    #         if i.right:
    #             path =tmp+"->"+str(i.right.val)
    #             allNodes.append((i.right,path))
    #         if not i.left and not i.right:
    #             paths.append(tmp)
    #
    #     return paths



if __name__ == "__main__":
    root = TreeNode(10)  # How to init a Tree  [10,5,-3,3,2,null,11,3,-2,null,1]
    root.insertLeft(5)
    root.insertRight(-3)
    left = root.getLeft()
    left.insertLeft(3)
    left.insertRight(2)
    right = root.getRight()
    right.insertRight(11)
    leftleft=left.getLeft()
    leftleft.insertLeft(3)
    leftleft.insertRight(-2)
    leftright = left.getRight()
    leftright.insertRight(1)
    answer = Solution()
    print(answer.pathSum(root,8))

