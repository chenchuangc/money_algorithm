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

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
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
            layer_avg = []
            for i in range(len(tmp)):
                count = 0
                for j in tmp[i]:
                    count = count+j
                layer_avg.append(count/len(tmp[i]))
            return layer_avg