# coding:utf-8
'''
选择排序法：
每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放到序列的起始位置，直到全部排完。
两个for循环即可，第二个for每循环一次找到最小元素的下标，然后放在最前面
'''

def selectSort(lists):
    count = len(lists)
    for i in range(count-1):
        min = i
        for j in range(i+1,count):
            if lists[j] < lists[min]:
                min = j
        lists[i],lists[min] = lists[min],lists[i]

    return lists

lists = [7, 8, 6, 2, 45, 5]
print selectSort(lists)

