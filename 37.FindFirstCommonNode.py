# -*- coding:utf-8 -*-
'''
输入两个链表，找出它们的第一个公共结点
思路：
1，先求出两个链表的长度
2，求两个链表的长度差 n
3，从较长链表的第 n+1 个开始和较短链表的头结点比较
4，得到相同的值即为所求
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Sloution():
    def FindFirstCommonNode(self,pHead1,pHead2):
        nLength1 = getListLength(pHead1)
        nLength2 = getListLength(pHead2)
        nLengthDiff = abs(nLength1-nLength2)

        if nLength1 > nLength2:
            pHeadLong = pHead1
            pHeadShort = pHead2
        else:
            pHeadLong = pHead2
            pHeadShort = pHead1

        for i in range(nLengthDiff):
            pHeadLong = pHeadLong.next

        while pHeadLong.next != None and pHeadShort.next != None and pHeadLong.next != pHeadShort.next:
            pHeadLong = pHeadLong.next
            pHeadShort = pHeadShort.next

        pFirstCommonNode = pHeadLong
        return pFirstCommonNode

    def getListLength(self,pHead):
        nLength = 0
        if pHead.next != None:
            nLength += 1
        return nLength


