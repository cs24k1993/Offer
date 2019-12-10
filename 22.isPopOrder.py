# coding: utf-8
'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

def isPopOrder(pushV,popV):
    if pushV == [] or popV == []:
        return False
    stack = []
    for i in pushV:
        stack.append(i)
        while len(stack) and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
    if len(stack):
        return False
    else:
        return True

pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
print(isPopOrder(pushV, popV))

