# coding:utf-8
'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
思路：递归


'''

class TreeNode(object):
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None
class Solution():
    def getTreeDepth(self,pRoot):
        if pRoot == None:
            return 0
        else:
            return max(self.getTreeDepth(pRoot.left),self.getTreeDepth(pRoot.right)) + 1

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

S = Solution()
print(S.getTreeDepth(pNode1))