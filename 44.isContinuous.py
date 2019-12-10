# -*- coding: utf-8 -*-
def isContinuous(list):
    if list == None or len(list) <= 0:
        return False
    transDict = {"A": 1, "J": 11, "Q": 12,  "K": 13}
    for i in range(len(list)):
        if list[i] in transDict.keys():
            list[i] = transDict[list[i]]

    list = sorted(list)
    numberOfZero = 0
    numberOfGap = 0

    # 统计0的个数
    i = 0
    while i < len(list) and list[i] == 0:
        numberOfZero += 1
        i += 1

    # 统计间隔数
    left = numberOfZero
    right = left + 1
    while right < len(list):
        # 出现对子，不可能是顺子
        if list[left] == list[right]:
            return False

        numberOfGap += list[right]  - list[left] - 1
        left = right
        right += 1

    return False if numberOfGap > numberOfZero else True

list = ['A', 3, 2, 5, 0]
list1= [8,9,10,'J','K']
print isContinuous(list1)