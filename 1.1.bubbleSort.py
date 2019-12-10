# coding:utf-8
'''
冒泡法：
第一趟：相邻的两数相比，大的往下沉。最后一个元素是最大的。
第二趟：相邻的两数相比，大的往下沉。最后一个元素不用比。
'''
def bubbleSort2(lists):

    count = len(lists)
    for i in range(count-1):
        for j in range(count-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists

lists = [7, 8, 6, 2, 10, 5]
print bubbleSort2(lists)

def bubbleSort(lists):

    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i]>lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

lists = [7, 8, 6, 2, 10, 5]
print bubbleSort(lists)