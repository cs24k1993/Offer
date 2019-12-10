# coding:utf-8
'''
思路：取一个元素p（通常是第一个元素，但是这是比较糟糕的选择），使元素p归位
（把p右边比p小的元素都放在它左边，在把空缺位置的左边比p大的元素放在p右边）；
列表被p分成两部分，左边都比p小，右边都比p大；
递归完成排序。
'''

def quickSort(array, left, right):
    if left > right:
        return 'Wrong number!!!'
    if right > len(array):
        return 'False right!!'
    if left < 0 or right < 0:
        return 'Wrong parameters'
    if array:
        if left < right:
            mid = partition(array, left, right)
            quickSort(array, left,  mid-1)
            quickSort(array, mid+1, right)
    else:
        return 'Empty array!!!'

def partition(array, left, right):
    tmp = array[left]
    while left < right:
        while left < right and array[right] >= tmp:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    return left

lists = [7, 8, 6, 2, 10, 5]
print quickSort(lists,0,5)
print lists

