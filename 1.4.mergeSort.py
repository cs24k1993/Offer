# coding:utf-8
'''
思路：一次归并：将现有的列表分为左右两段，将两段里的元素逐一比较，
小的就放入新的列表中。比较结束后，新的列表就是排好序的。然后递归。
（归并两段时，两段都已经是排序好的，刚开始不是排序的，递归直到都是
两个单个元素，然后排序）
'''

def merge(array, low, mid, high):
    tmp = []
    i = low
    j = mid +1
    while i <= mid and j <= high:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while i <= mid:
        tmp.append(array[i])
        i += 1
    while j <= high:
        tmp.append(array[j])
        j += 1
    array[low:high+1] = tmp

def mergeSort(array, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(array, low, mid)
        mergeSort(array, mid+1, high)
        merge(array, low, mid, high)

lists = [7, 8, 6, 2, 10, 5]
print mergeSort(lists,0,5)
print lists