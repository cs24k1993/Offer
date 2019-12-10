# -*- coding: utf-8 -*-
def Permutation(string):
    if not len(string):
        return []
    if len(string) == 1:
        return list(string)
    charList = list(string)
    charList.sort()   # 先排序，在后面对重复字符的判断方便，不然情况复杂很多
    pStr = []
    for i in range(len(charList)):
        if i > 0 and charList[i] == charList[i-1]:
            continue
        temp = Permutation("".join(charList[:i]) + "".join(charList[i+1:]))
        for j in temp:
            pStr.append(charList[i] + j)
    return pStr

string = "aba"
print Permutation(string)