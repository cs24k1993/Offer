# -*- coding:utf-8 -*-
def searchFirstNotRepeatChar(str):
    if str == None or len(str) <= 0:
        return -1
    strList = list(str)
    charDict = {}
    for i in strList:
        if i not in charDict.keys():
            charDict[i] = 0
        charDict[i] += 1
    print charDict  # charDict的顺序？怎么能保证charDict[j] == 1的字符是第一次出现而不是第二次出现的？

    for j in strList:
        if charDict[j] == 1:
            return j
    return -1

str = "agbfcace"
print searchFirstNotRepeatChar(str)