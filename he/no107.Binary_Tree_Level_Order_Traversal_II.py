'''
执行用时 :36 ms, 在所有 Python3 提交中击败了85.03%的用户
内存消耗 :12.9 MB, 在所有 Python3 提交中击败了88.07%的用户
'''
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x:int):
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
    def levelOrderBottom(self, root: TreeNode):
        if root is None: return []
        else:
            allNodes = []
            tmp = []
            allNodes.append([root])
            tmp.append([root.val])

            while(allNodes !=[]):
                tmp_layer = allNodes.pop()
                tmp_layer2 = []
                tmp_layer_val = []

                for i in tmp_layer:
                    if i.left is not None:
                        tmp_layer2.append(i.left)
                        tmp_layer_val.append(i.left.val)
                    if i.right is not None:
                        tmp_layer2.append(i.right)
                        tmp_layer_val.append(i.right.val)
                if tmp_layer2 != []:
                    allNodes.append(tmp_layer2)
                    tmp.append(tmp_layer_val)
            result = []
            for i in range(len(tmp)-1,-1,-1):
                result.append(tmp[i])
            return result

if __name__ == "__main__":
    for i in range(9, -1,-1):
        print(i)