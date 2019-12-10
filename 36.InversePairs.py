# -*- coding:utf-8 -*-
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
思路：拷贝该数组后对拷贝的数组排序。计算数组中的最小值在原始数组中出现的位置，
统计原始数组中最小值前面的个数，之后在原始数组中去掉最小值。重复上述步骤。
'''

def InversePairs(data):
    if len(data) < 0:
        return
    copy = []
    for i in range(len(data)):
        copy.append(data[i])
    copy.sort()

    count = 0
    i = 0
    while len(copy) > i:  # 这里如果用len(data)，结果也是3，为什么？
        count += data.index(copy[i])
        data.remove(copy[i])
        i += 1
    return count

print InversePairs([2,3,4,1])
