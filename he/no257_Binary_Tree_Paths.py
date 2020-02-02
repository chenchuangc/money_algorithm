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

    def construct_paths(self, root: TreeNode, path: str, paths: List[str]):
        # 列表paths是一个引用
        if root:
            path += str(root.val)
            if not root.left and not root.right:  # 当前节点是叶子节点
                paths.append(path)  # 把路径加入到答案中
                # print(paths)
            else:
                path += '->'  # 当前节点不是叶子节点，继续递归遍历
                self.construct_paths(root.left, path, paths)
                self.construct_paths(root.right, path, paths)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 作者：LeetCode
        # 链接：https: // leetcode - cn.com / problems / binary - tree - paths / solution / er - cha - shu - de - suo - you - lu - jing - by - leetcode /
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        paths = []
        self.construct_paths(root, '', paths)
        return paths

    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        allNodes = []    # stack
        allNodes.append((root,str(root.val))) # stack把路径和节点绑定在一起

        while(allNodes != []):
            i,tmp=allNodes.pop()
            if i.left:
                path =tmp+"->"+str(i.left.val)
                allNodes.append((i.left,path))

            if i.right:
                path =tmp+"->"+str(i.right.val)
                allNodes.append((i.right,path))
            if not i.left and not i.right:
                paths.append(tmp)

        return paths



if __name__ == "__main__":
    root = TreeNode(1)  # How to init a Tree
    root.insertLeft(2)
    root.insertRight(3)
    left = root.getLeft()

    left.insertRight(5)
    answer = Solution()
    print(answer.binaryTreePaths2(root))

