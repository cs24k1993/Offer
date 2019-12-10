# coding:utf-8
'''
思路：列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
一个for循环，一个while循环即可。每经过一次while循环把元素插入到正确的位置。
'''

def insertSort(lists):
    count = len(lists)
    for i in range(1,count):
        j = i - 1
        min = lists[i]
        while j >= 0 and lists[j] > min:
            lists[j+1] = lists[j]
            j = j - 1
        lists[j+1] = min
    return lists

lists = [7, 8, 6, 2, 10, 5]
print insertSort(lists)