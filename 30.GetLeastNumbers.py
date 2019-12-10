# import sys
# sys.path.append("D:\PythonProgram\Offer")
# from heapSort import heapSort
def sift(lists,left,right):
    i = left
    j = 2*i + 1
    temp = lists[i]
    while j <= right:
        if j < right and lists[j] > lists[j+1]:
            j = j + 1
        if temp > lists[j]:
            lists[i] = lists[j]
            i = j
            j = 2*i + 1
        else:
            break
    lists[i] = temp

def heapSort(lists):
    n = len(lists)
    for i in range(n // 2 - 1,-1,-1):
        sift(lists, i, n-1)

    for i in range(n-1,-1,-1):
        lists[0],lists[i] = lists[i],lists[0]
        sift(lists,0,i-1)
    return  lists


def GetLeastNumbers(lists,k):
    output = []
    n = len(lists)
    if k <= 0 or k > n or n <= 0:
        return []
    for i in range(n):
        if len(output) < k:
            output.append(lists[i])
        else:
            output = heapSort(output)
            if lists[i] >= output[0]:
                continue
            else:
                output[0] = lists[i]
    return output[::-1]

lists=[4,5,1,6,2,7,3,8]
print GetLeastNumbers(lists,5)