# coding:utf-8
'''
希尔排序是一种分组插入排序算法。
首先取一个整数d1=n/2，将元素分为d1个组，每组相邻量元素之间距离为d1，在各组内进行直接插入排序；
取第二个整数d2=d1/2，重复上述分组排序过程，直到di=1，
即所有元素在同一组内进行直接插入排序。希尔排序每趟并不使某些元素有序，
而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。
'''
def shellSort(lists):
    n = len(lists)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            tmp = lists[i]
            j = i - gap
            while j >= 0 and tmp < lists[j]:
                lists[j + gap] = lists[j]
                j = j - gap
            lists[j + gap] = tmp
        gap = gap // 2

    return lists

lists = [5,3,8,4,1,6,2,9]
print shellSort(lists)
