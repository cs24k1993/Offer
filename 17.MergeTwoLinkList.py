# coding:utf-8
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self,pHead1,pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1

        pMergeHead = None
        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next,pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1,pHead2.next)

        return pMergeHead


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
pMergeHead = S.Merge(node1, node4)
while pMergeHead:
    print pMergeHead.val
    pMergeHead = pMergeHead.next
