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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = self.binaryTreePaths(root)
        results = []
        for i in paths:
            i = [int(j) for j in i.split()]
            s = 0
            for j in i:s+=j
            if s==sum:results.append(i)
        return results
    def construct_paths(self, root: TreeNode, path: str, paths: List[str]):
        # 列表paths是一个引用
        if root:
            path=path+' '+str(root.val)
            if not root.left and not root.right:  # 当前节点是叶子节点
                paths.append(path)  # 把路径加入到答案中
                # print(paths)
            else:

                self.construct_paths(root.left, path, paths)
                self.construct_paths(root.right, path, paths)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.construct_paths(root, '', paths)
        return paths

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
    root = TreeNode(1)  # How to init a Tree
    root.insertLeft(2)
    root.insertRight(3)
    left = root.getLeft()

    left.insertRight(5)
    answer = Solution()
    print(answer.pathSum(root,4))

