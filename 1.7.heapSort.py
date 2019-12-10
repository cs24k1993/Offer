# coding:utf-8
'''
步骤：
　　建立堆
　　得到堆顶元素，为最大元素
　　去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
　　堆顶元素为第二大元素。
　　重复步骤3，直到堆变空。
'''
def sift(lists,left,right):
    i = left
    j = 2*i + 1
    temp = lists[i]
    while j <= right:
        if j < right and lists[j] < lists[j+1]:
            j = j + 1
        if temp < lists[j]:
            lists[i] = lists[j]
            i = j
            j = 2*i + 1
        else:
            break
    lists[i] = temp

def heapSort(lists):
    n = len(lists)
    # 建堆，从最后一个有孩子的父亲开始，直到根节点
    for i in range(n // 2 - 1,-1,-1):
        sift(lists, i, n-1)

    for i in range(n-1,-1,-1):
        # 把根节点和调整的堆的最后一个元素交换
        lists[0],lists[i] = lists[i],lists[0]
        # 再调整，从0到i-1
        sift(lists,0,i-1)

    return  lists

lists = [5,3,8,4,1,6,2,9]
print heapSort(lists)
















