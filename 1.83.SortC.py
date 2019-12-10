# coding:utf-8
# 借用一个辅助数组，正负交替

def sortC(lists):
    count = len(lists)
    arr = []
    p = 0
    n = 0
    while p < count and n < count:
        while p < count and lists[p] < 0:
            p = p + 1
        while n < count and lists[n] > 0 :
            n = n + 1
        if p >= count or n >= count:
            break
        arr.append(lists[p])
        arr.append(lists[n])
        p = p + 1
        n = n + 1

    if p >= count:
        while n < count:
            if lists[n] < 0:
                arr.append(lists[n])
            n = n + 1

    if n >= count:
        while p < count:
            if lists[p] > 0:
                arr.append(lists[p])
            p = p + 1

    return arr

lists = [-2,-1,3,-5,2,7,-4,5]
print sortC(lists)

