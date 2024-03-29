# coding:utf-8
'''
反转链表，需要三个指针
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def ReverseList(head):
    if head == None or head.next == None:
        return head
    pre = None
    cur = head
    temp = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

head=ListNode(1)      #测试代码
p1=ListNode(2)      #建立链表1->2->3->4->None;
p2=ListNode(3)
p3=ListNode(4)
head.next=p1
p1.next=p2
p2.next=p3
p=ReverseList(head)   #输出链表 4->3->2->1->None

while p:
    print p.val
    p = p.next



