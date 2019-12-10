# coding:utf-8
'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
相当于按层遍历, 中间需要队列做转存
打印一个节点的值时，应该把该节点左右节点存储到队列中
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printBinaryTree(self,root):
        if not root:
            return
        result = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.printBinaryTree(pNode1))