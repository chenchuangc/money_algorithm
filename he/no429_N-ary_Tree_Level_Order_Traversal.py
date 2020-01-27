"""
# Definition for a Node.
执行用时 :44 ms, 在所有 Python3 提交中击败了99.81%的用户
内存消耗 :14.9 MB, 在所有 Python3 提交中击败了60.68%的用户
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root: 'Node'):
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
                    for j in i.children:
                        if j is not None:
                            tmp_layer2.append(j)
                            tmp_layer_val.append(j.val)
                if tmp_layer2 != []:
                    allNodes.append(tmp_layer2)
                    tmp.append(tmp_layer_val)
            return tmp