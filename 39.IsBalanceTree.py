# coding:utf-8
'''
判断平衡二叉树
问题：会重复遍历二叉树的节点，怎么优化？
'''
class TreeNode():
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None

class Solution():
    def getDepth(self,pRoot):
        if pRoot == None:
            return 0
        return max(self.getDepth(pRoot.left), self.getDepth(pRoot.right)) + 1

    def isBalanceTree(self,pRoot):
        if pRoot == None:
            return True
        if abs(self.getDepth(pRoot.left) - self.getDepth(pRoot.right)) > 1:
            return False
        return self.isBalanceTree(pRoot.left) and self.isBalanceTree(pRoot.right)

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)
# pNode8 = TreeNode(8)
# pNode9 = TreeNode(9)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7
# pNode7.left = pNode8
# pNode8.left = pNode9

S = Solution()
print(S.isBalanceTree(pNode1))